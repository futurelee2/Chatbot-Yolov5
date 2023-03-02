<div align= "center">
  <img width="850" src="https://i.esdrop.com/d/f/CcSudjZ5R8/permf9tpHa.png">
</div>
<br>
<br>


<h2> 📊 프로젝트 개요 </h2>

<div align= "center">
  <img width="850" src = "https://i.esdrop.com/d/f/CcSudjZ5R8/Tov2sHONfa.png">
</div>
<br>

2021년 기준 1인가구의 수는 전체 인구의 33.4%로 약 700만 가구입니다.
그리고 5년간 1인가구의 비율이 매년 증가하고 있음을 확인 할 수 있습니다.

1인가구가 겪는 첫 번째 어려움은 심리적 불안감과 외로움이고, 두 번째는 아플 때의 보호자의 부재입니다. 
이처럼 정서적 결핍이 우울증으로 발전되거나, 낙상사고처럼 응급처지가 필요한 상황에서 도움을 받지 못해 고독사로 이어지는 경우가 있습니다.


앞서 설명한 배경을 토대로 프로젝트의 목적을 크게 두 가지로 나눴습니다.
첫째는 <챗봇>을 통해 청년에게는 격려와 응원의 메세지를, 노년에게는 말벗이 되어주어 1인가구의 우울증을 개선해주고,
챗봇에 입력한 메시지에서 심각한 불안증세가 보일 경우, 지인에게 위급상황을 알려주어 도움을 요청하는 것입니다.

둘째는 가구 내 화재 또는 낙상이 발생 할 경우 ‘카카오톡’ 알림서비스를 통해 신속하게 대처할 수 있도록 도와주고,
장시간 집을 비웠을 때 실시간 확인을 통한 1인가구의 사용자의 불안감 해소가 목적입니다.

<br>
<br>

<h2> 🔌코드 실행 </h2>

```python
pip install -r requirements.txt
```

<h5> 챗봇 학습 </h5>

```python
# python train_torch.py --train --gpus 1 --max_epochs 15
```
<h6> 해당 코드를 통해 데이터를 학습시켜 CheckPoint를 만들어냅니다.<br><br>
     만든 CheckPoint는 --chat 명령어를 사용하는데 이용됩니다. <br><br><br>
</h6> 

<h5> YOLO 학습 </h5>

```python
python ./Yolov5/train.py --data ./fall_dataset/data.yaml --epochs 100 --weights ./yolov5s.pt --batch-size 64 --img 640
```

<h6> 해당 코드를 입력하면 코드에 들어있는 규칙에 맞는.pt 파일을 만들어줍니다.<br><br>
     --data 에는 본인들이 사용할 이미지 데이터셋과 라벨로 구성된 .yaml파일 이름을 넣어주면 됩니다. <br><br>
     --weight는 기존의 Pre-Trained 모델로, 다양한 모델이 있지만 해당 프로젝트는 실시간 감지가 가장 주가 되기 때문에, yolov5s.pt를 사용했습니다.<br><br><br>
</h6>
     
     

<h5> 웹사이트로 들어가기 </h5>



```python
if __name__ == '__main__':
    # app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
    app.run(host="0.0.0.0", debug=True, port=int(os.environ.get("PORT", 5000)))
```

<h6> app_flask_chatbot.py 내의 코드로, Flask를 통한 웹사이트가 생성됩니다. <br><br>
     웹사이트는 해당 레퍼지토리의 Templetes, static 폴더 내의 파일을 수정하여 수정할 수 있습니다. <br><br>
     사이트 내에 있는 각 카테고리의 사진을 누르게 되면 챗봇 또는 실시간 감지창으로 넘어가게 됩니다. <br><br><br>
</h6>


<h2> 👭 위로형 챗봇 : 한우리 </h2>

  <p>
<div>

<details>
<summary><b>환경 및 데이터셋</b></summary>
<div align= "center">
  <img width="850" src = "https://i.esdrop.com/d/f/CcSudjZ5R8/zDcvLE5rBt.png">
</div>
  <h5>구축 환경 </h5>
  <h6>Python 3.8 / Google Colab </h6>
  <h5>데이터셋</h5>
  <h6>챗봇의 데이터셋은 <'AI HUB'의 감성 대화 말뭉치>와 <웰니스 챗봇 데이터> 2가지를 활용하여 데이터셋을 구성했습니다.<br><br>
      데이터셋은 총 3개의 라벨로 구성되어 있으며, 라벨의 기준은 문장을 감정으로 분류하여 일상, 부정, 긍정으로 나누었습니다.<br><br><br>
  </h6>
  <p>
</details>
<details>
<summary><b>모델 학습</b></summary>
<div align= "center">
  <img width="850" src = "https://i.esdrop.com/d/f/CcSudjZ5R8/o5VYftQBrI.png">
</div>
  <h5> 모델 학습 과정 </h5>
  <h6> 데이터양, 라벨의 수, max_len 총 3가지를 수정하여 3회 정도 모델 학습을 진행하였습니다. <br><br>
       최종적으로 사용한 모델은 데이터량 약 236,000개 / 라벨 총 3개 / max_len = 64 입니다. <br><br><br>
  </h6>
  
</div>
</details>
<details>
<summary><b>알고리즘</b></summary>
<div align= "center">
  <img width="850" src = "https://i.esdrop.com/d/f/CcSudjZ5R8/lY4MTWLTed.png">
</div>
  
</details>

<h2> 🔥 화재 및 낙상 감지 </h2>
 

<details>
<summary><b>환경 및 데이터셋</b></summary>
<div align= "center">
  <img width="850" src = "https://i.esdrop.com/d/f/CcSudjZ5R8/a2kd3yvFF0.png">
</div>
  <h5>구축 환경 </h5>
  <h6>Python 3.8 / Google Colab </h6>
  <h5>데이터셋</h5>
  <h6>Yolo의 데이터셋은 <'AI HUB' 화재 발생 예측 영상>, <'GitHub' Fire-detection dataset>, <'AI HUB' 시니어 이상행동 영상>, <'Kaggle' Fall Detection Dataset> 총 4가지를 활       용하여 데이터셋을 구성했습니다.<br><br>
      데이터셋은 이미지와 라벨링 데이터 한쌍으로 구성되어 있으며, 라벨링 데이터는 Label, CenterX, CenterY, Width, Height로 구성되어 있는 Yolo TXT 형태여야 합니다. <br><br>
      해당 데이터셋 구성을 위해 COCO Json to Yolo Txt과 XML을 사용하여 로보플로우로 해당 라벨링 데이터를 만드는 방식을 선택했습니다.<br><br>
      라벨링은 유사 상황 감지를 위해 총 13개로 구성되어 있으며, 실제 화재 및 낙상 감지 라벨은 2개입니다. <br><br><br>
  </h6>
</details>
<details>
<summary><b>모델 학습</b></summary>
<div align= "center">
  <img width="850" src = "https://i.esdrop.com/d/f/CcSudjZ5R8/XWOHrkqMgU.png">
</div>
  <h5>모델 학습 과정 </h5>
  <h6> 모델 학습 방식은 Pre-Trained Model 파일에 파인튜닝 하는 방식으로 진행했습니다. <br><br>
       해당 프로젝트는 실시간 감지를 목적으로 했기 때문에 v5s 모델을 선택하여 파인튜닝을 진행했습니다. <br><br>
       batch-size=64, epochs=100 로 학습을 진행하였으며,
       epochs=84일 때 가장 좋은 모델이 생성되었으며, 'metric/mAP_0.5:0.95' 값이 0.619로 100번의 학습 과정동안 가장 높게 나왔습니다.
       최종 학습이 종료된 후 나온 결과값은 다음과 같습니다.
<div align= "center">
  <img width="850" src = "https://i.esdrop.com/d/f/CcSudjZ5R8/5QFgM6YsBY.png">
</div>       
  
<br><br><br>
  </h6>
</details>
<details>
<summary><b>알고리즘</b></summary>
<div align= "center">
  <img width="850" src = "https://i.esdrop.com/d/f/CcSudjZ5R8/uAsZeo66Tk.png">
</div>
</details>

- - -
<div align = "center">
<h4> 💽Tech Stack 💽 </h4>
🚋 Plaforms & Languages 💬
<br><br>
<img src = "https://img.shields.io/static/v1?label=Python&message=v3.8&color=red">
<img src = "https://img.shields.io/static/v1?label=Flask&message=2.2.2&color=orange">
<img src = "https://img.shields.io/static/v1?label=Matplotlib&message=3.5.3&color=yellow">
<br>
<img src = "https://img.shields.io/static/v1?label=Numpy&message=1.21.6&color=green">
<img src = "https://img.shields.io/static/v1?label=Opencv-python&message=4.7.0.68&color=blue">
<img src = "https://img.shields.io/static/v1?label=Pandas&message=1.3.5&color=navy">
<img src = "https://img.shields.io/static/v1?label=Torch&message=1.13.1&color=purple">
<br>
<img src = "https://img.shields.io/static/v1?label=&message=HTML&color=brightgreen">
<img src = "https://img.shields.io/static/v1?label=&message=JavaScript&color=coral">
</div>
