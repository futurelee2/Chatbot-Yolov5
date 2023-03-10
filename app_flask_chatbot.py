from flask import Flask, render_template, Response, request, jsonify

import argparse
import platform
from pathlib import Path
import os
import torch

from Yolov5.models.common import DetectMultiBackend
from Yolov5.utils.dataloaders import IMG_FORMATS, VID_FORMATS, LoadImages, LoadScreenshots, LoadStreams
from Yolov5.utils.general import (LOGGER, Profile, check_file, check_img_size, check_imshow, colorstr, cv2,
                                increment_path, non_max_suppression, scale_boxes, strip_optimizer, xyxy2xywh)
from Yolov5.utils.plots import Annotator, colors, save_one_box
from Yolov5.utils.torch_utils import select_device, smart_inference_mode

from Chatbot.model.chatbot.kogpt2 import chatbot as ch_kogpt2
from Yolov5.kakao import kakao_message_to_friends_location_fall, kakao_message_to_friends_location_chatbot, kakao_message_to_friends_location_fire, kakao_message_to_me_location_fire
from Yolov5.kakao import kakao_utils, kakao_utils_friends

app = Flask(__name__)


# Yolo에서 메세지가 발송될 시에 False로 바뀌고, 화면에 미검출 시에 다시 True로 바뀜.
yolo_message_available = True

# Stopwords의 개념으로 우울증울 짐작할 수 있는 단어 보따리.
# 해당 단어가 들어간 문장이 입력될 때 마다 chatbot_count가 1회씩 증가. 7회 이상 입력될 경우, 지인에게 위험 문자 발송.
chatbot_count = 0
ultra_negative_words= ['자살', '살인', '불안', '짜증', '울적', '세상', '왕따', '지옥', '천국', '우울증', '소외감', '한심', '개새끼', '씨발', '병신',
                       '죽고', '죽을', '죽이고', '외로워', '외롭다', '외로운', '끔찍해', '끔찍하다', '끔찍해', '버림받', '역겹다', '역겨워', '역겨운', '쓸쓸', '밉다', '미워', '미운',
                       '한심한', '끔찍한', '버려진' '식욕' ]

@smart_inference_mode()
def run():

    global yolo_message_available

    weights = './Yolov5/best.pt'  # model path or triton URL
    source = 0  # file/dir/URL/glob/screen/0(webcam)
    data = './data/coco128.yaml'  # dataset.yaml path
    imgsz = (640, 640)  # inference size (height, width)
    conf_thres = 0.4  # confidence threshold
    iou_thres = 0.45  # NMS IOU threshold
    max_det = 1000  # maximum detections per image
    device = ''  # cuda device, i.e. 0 or 0,1,2,3 or cpu
    view_img = False  # show results
    save_txt = False  # save results to *.txt
    save_conf = False  # save confidences in --save-txt labels
    save_crop = False  # save cropped prediction boxes
    nosave = False  # do not save images/videos
    classes = None  # filter by class: --class 0, or --class 0 2 3 fire falldown
    agnostic_nms = False  # class-agnostic NMS
    augment = False  # augmented inference
    visualize = False  # visualize features
    update = False  # update all models
    project = 'Yolov5/runs/detect'  # save results to project/name
    name = 'exp'  # save results to project/name
    exist_ok = False  # existing project/name ok, do not increment
    line_thickness = 3  # bounding box thickness (pixels)
    hide_labels = False  # hide labels
    hide_conf = False  # hide confidences
    half = False  # use FP16 half-precision inference
    dnn = False  # use OpenCV DNN for ONNX inference
    vid_stride = 1  # video frame-rate stride


    source = str(source)
    save_img = not nosave and not source.endswith('.txt')  # save inference images
    is_file = Path(source).suffix[1:] in (IMG_FORMATS + VID_FORMATS)
    is_url = source.lower().startswith(('rtsp://', 'rtmp://', 'http://', 'https://'))
    webcam = source.isnumeric() or source.endswith('.streams') or (is_url and not is_file)
    screenshot = source.lower().startswith('screen')
    if is_url and is_file:
        source = check_file(source)  # download

    # Directories
    save_dir = Path(increment_path(Path(project) / name, exist_ok=exist_ok))  # increment run
    (save_dir / 'labels' if save_txt else save_dir).mkdir(parents=True, exist_ok=True)  # make dir

    # Load model
    device = select_device(device)
    model = DetectMultiBackend(weights, device=device, dnn=dnn, data=data, fp16=half)
    stride, names, pt = model.stride, model.names, model.pt
    imgsz = check_img_size(imgsz, s=stride)  # check image size
    message_available = True



    # Dataloader
    bs = 1  # batch_size
    if webcam:
        view_img = check_imshow(warn=True)
        dataset = LoadStreams(source, img_size=imgsz, stride=stride, auto=pt, vid_stride=vid_stride)
        bs = len(dataset)
    elif screenshot:
        dataset = LoadScreenshots(source, img_size=imgsz, stride=stride, auto=pt)
    else:
        dataset = LoadImages(source, img_size=imgsz, stride=stride, auto=pt, vid_stride=vid_stride)
    vid_path, vid_writer = [None] * bs, [None] * bs

    # Run inference
    model.warmup(imgsz=(1 if pt or model.triton else bs, 3, *imgsz))  # warmup
    seen, windows, dt = 0, [], (Profile(), Profile(), Profile())
    for path, im, im0s, vid_cap, s in dataset:
        with dt[0]:
            im = torch.from_numpy(im).to(model.device)
            im = im.half() if model.fp16 else im.float()  # uint8 to fp16/32
            im /= 255  # 0 - 255 to 0.0 - 1.0
            if len(im.shape) == 3:
                im = im[None]  # expand for batch dim

        # Inference
        with dt[1]:
            visualize = increment_path(save_dir / Path(path).stem, mkdir=True) if visualize else False
            pred = model(im, augment=augment, visualize=visualize)

        # NMS
        with dt[2]:
            pred = non_max_suppression(pred, conf_thres, iou_thres, classes, agnostic_nms, max_det=max_det)

        # Second-stage classifier (optional)
        # pred = utils.general.apply_classifier(pred, classifier_model, im, im0s)

        # Process predictions
        for i, det in enumerate(pred):  # per image
            seen += 1
            if webcam:  # batch_size >= 1
                p, im0, frame = path[i], im0s[i].copy(), dataset.count
                s += f'{i}: '
            else:
                p, im0, frame = path, im0s.copy(), getattr(dataset, 'frame', 0)

            p = Path(p)  # to Path
            save_path = str(save_dir / p.name)  # im.jpg
            txt_path = str(save_dir / 'labels' / p.stem) + ('' if dataset.mode == 'image' else f'_{frame}')  # im.txt
            s += '%gx%g ' % im.shape[2:]  # print string
            gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
            imc = im0.copy() if save_crop else im0  # for save_crop
            annotator = Annotator(im0, line_width=line_thickness, example=str(names))
            if len(det):
                # Rescale boxes from img_size to im0 size
                det[:, :4] = scale_boxes(im.shape[2:], det[:, :4], im0.shape).round()

                # Print results
                for c in det[:, 5].unique():
                    n = (det[:, 5] == c).sum()  # detections per class
                    s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string

                # Write results
                for *xyxy, conf, cls in reversed(det):
                    if save_txt:  # Write to file
                        xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()  # normalized xywh
                        line = (cls, *xywh, conf) if save_conf else (cls, *xywh)  # label format
                        with open(f'{txt_path}.txt', 'a') as f:
                            f.write(('%g ' * len(line)).rstrip() % line + '\n')

                    if save_img or save_crop or view_img:  # Add bbox to image
                        c = int(cls)  # integer class
                        label = None if hide_labels else (names[c] if hide_conf else f'{names[c]} {conf:.2f}')
                        # 검출 대상의 conf가 0.4가 넘을 경우, 해당 코드 진행
                        if conf > 0.4:
                            annotator.box_label(xyxy, label, color=colors(c, True))
                            # 검출 클래스가 불 일 경우,
                            if names[c] == 'fire' :
                                if yolo_message_available == True:
                                    kakao_message_to_friends_location_fire.send_message_to_friends_location_fire()
                                    kakao_message_to_me_location_fire.send_message_to_me_location_fire()
                                    yolo_message_available = False
                                print(yolo_message_available)

                            # 검출 클래스가 낙상일 경우,
                            if names[c] == 'falldown':
                                if yolo_message_available == True:
                                    kakao_message_to_friends_location_fall.send_message_to_friends_location_fall()
                                    yolo_message_available = False
                                print('debug_01',yolo_message_available)


                    if save_crop:
                        save_one_box(xyxy, imc, file=save_dir / 'crops' / names[c] / f'{p.stem}.jpg', BGR=True)

            # Stream results
            im0 = annotator.result()
            if view_img:
                if platform.system() == 'Linux' and p not in windows:
                    windows.append(p)
                    cv2.namedWindow(str(p), cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)  # allow window resize (Linux)
                    cv2.resizeWindow(str(p), im0.shape[1], im0.shape[0])
                # cv2.imshow('dfd', im0) # 프로그램으로 보기
                # HTML에 들어갈수 있게, 인코딩하는 과정.
                ret, buffer = cv2.imencode(".jpeg", im0)
                frame = buffer.tobytes()
                yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
                cv2.waitKey(1)  # 1 millisecond

            # Save results (image with detections)
            if save_img:
                if dataset.mode == 'image':
                    cv2.imwrite(save_path, im0)
                else:  # 'video' or 'stream'
                    if vid_path[i] != save_path:  # new video
                        vid_path[i] = save_path
                        if isinstance(vid_writer[i], cv2.VideoWriter):
                            vid_writer[i].release()  # release previous video writer
                        if vid_cap:  # video
                            fps = vid_cap.get(cv2.CAP_PROP_FPS)
                            w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                            h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                        else:  # stream
                            fps, w, h = 30, im0.shape[1], im0.shape[0]
                        save_path = str(Path(save_path).with_suffix('.mp4'))  # force *.mp4 suffix on results videos
                        vid_writer[i] = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
                    vid_writer[i].write(im0)

        # Print time (inference-only)
        LOGGER.info(f"{s}{'' if len(det) else '(no detections), '}{dt[1].dt * 1E3:.1f}ms")

        # 검출 대상이 하나도 없을 경우, 다시 message를 보낼 수 있도록 함.
        if len(det) == 0:
            yolo_message_available = True
            print('debug_02 : ',yolo_message_available)

    # Print results
    t = tuple(x.t / seen * 1E3 for x in dt)  # speeds per image
    LOGGER.info(f'Speed: %.1fms pre-process, %.1fms inference, %.1fms NMS per image at shape {(1, 3, *imgsz)}' % t)
    if save_txt or save_img:
        s = f"\n{len(list(save_dir.glob('labels/*.txt')))} labels saved to {save_dir / 'labels'}" if save_txt else ''
        LOGGER.info(f"Results saved to {colorstr('bold', save_dir)}{s}")
    if update:
        strip_optimizer(weights[0])  # update model (to fix SourceChangeWarning)




@app.route('/')
def hello():
    return render_template ("index.html")

@app.route('/yolo')
def yolo():
    return render_template ("yolo.html")

@app.route('/yolo_start')
def yolo_start():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(run(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/chatbot')
def chat():
    return render_template ("chatbot.html")

@app.route('/res', methods=['POST'])
def ajax():
    data = request.get_json()
    text = data['messageText']
    global ultra_negative_words
    global chatbot_count
    for i in range(len(ultra_negative_words)):
        if ultra_negative_words[i] in text:
            chatbot_count += 1
            print(chatbot_count)
            if chatbot_count >= 7:
                kakao_message_to_friends_location_chatbot.send_message_to_friends_location_chatbot()
                chatbot_count = 0
    print(data)
    print(type(data),data['messageText'])
    answer = ch_kogpt2.predict(data['messageText'])
    return jsonify({
        "answer": answer
    })



if __name__ == '__main__':
    # app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
    app.run(host="0.0.0.0", debug=True, port=int(os.environ.get("PORT", 5000)))

