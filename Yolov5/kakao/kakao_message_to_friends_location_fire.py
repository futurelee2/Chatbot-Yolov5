# 친구에게 위치 템플릿으로 카톡보내기
# 낙상

import requests
import json
import os
import glob
from Yolov5.kakao import kakao_utils_friends
import sys



def send_message_to_friends_location_fire():
    KAKAO_TOKEN_FILENAME = "./kakao_code.json"  # "<kakao_token.json 파일이 있는 경로를 입력하세요.>"
    KAKAO_APP_KEY = "" # 어플의 REST KEY 넣어주면 됩니다.
    tokens = kakao_utils_friends.update_tokens(KAKAO_APP_KEY, KAKAO_TOKEN_FILENAME)
    headers={"Authorization" : "Bearer " + tokens["access_token"]}

    friend_url = "https://kapi.kakao.com/v1/api/talk/friends"

    result = json.loads(requests.get(friend_url, headers=headers).text)

    friends_list = result.get("elements")

    for i in range(len(friends_list)):
        friend_id = friends_list[i].get("uuid")

        print(friend_id)
        send_url= "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"

        template = {
            "object_type": "location",
            "content": {
                "title": "🔥긴급!! 화재가 발생했습니다!!🔥",
                "description": "집에 불이 났어요!!!!!",
                "image_url": "https://i.esdrop.com/d/f/NXl6YkfhTU/1mhWuevedC.png",
                "image_width": 800,
                "image_height": 800,
                "link": {
                    "web_url": "https://developers.kakao.com",
                    "mobile_web_url": "https://developers.kakao.com/mobile",
                    "android_execution_params": "platform=android",
                    "ios_execution_params": "platform=ios"
                }
            },
            "buttons": [
                {
                    "title": "웹으로 보기",
                    "link": {
                        "web_url": "https://developers.kakao.com",
                        "mobile_web_url": "https://developers.kakao.com/mobile"
                    }
                }
            ],
            "address": "서울 중구 퇴계로 166",
            "address_title": "흥국빌딩 2층 아시아경제 교육센터"
        }
        response = requests.post(send_url, headers=headers, data=template)
        response.status_code
    backup_filename = glob.glob('D:/asdf/work/python/Chatbot-Yolov5/kakao_code.json.*')
    print(backup_filename)
    for f in backup_filename:
        os.remove(f)



# # 친구에게 위치 템플릿으로 카톡보내기
#
# import requests
# import json
# import glob
# import os
#
# from Yolov5.kakao import kakao_utils_friends
#
#
# def send_message_to_friends_location_fire():
#     global yolo_message_available
#     while yolo_message_available:
#         KAKAO_TOKEN_FILENAME = "./kakao_code.json"  # "<kakao_token.json 파일이 있는 경로를 입력하세요.>"
#         KAKAO_APP_KEY = "6188bf2cdc11ad8bb911d6ef9e0bcd46"
#         tokens = kakao_utils_friends.update_tokens(KAKAO_APP_KEY, KAKAO_TOKEN_FILENAME)
#         headers={"Authorization" : "Bearer " + tokens["access_token"]}
#
#         friend_url = "https://kapi.kakao.com/v1/api/talk/friends"
#
#         result = json.loads(requests.get(friend_url, headers=headers).text)
#
#         friends_list = result.get("elements")
#
#         friend_id = friends_list[0].get("uuid")
#
#         send_url= "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"
#
#         template={
#             'receiver_uuids': '["{}"]'.format(friend_id),
#             "template_object": json.dumps({
#                 "object_type": "location",
#                 "content": {
#                     "title": "흥국빌딩 2층 아시아경제 교육센터",
#                     "description": "흥국빌딩 2층 아시아경제 교육센터 위치입니다.",
#                     "image_url": "https://i.esdrop.com/d/f/NXl6YkfhTU/1mhWuevedC.png",
#                     "image_width": 800,
#                     "image_height": 800,
#                     "link": {
#                         "web_url": "https://developers.kakao.com",
#                         "mobile_web_url": "https://developers.kakao.com/mobile",
#                         "android_execution_params": "platform=android",
#                         "ios_execution_params": "platform=ios"
#                     }
#                 },
#                 "buttons": [
#                     {
#                         "title": "웹으로 보기",
#                         "link": {
#                             "web_url": "https://developers.kakao.com",
#                             "mobile_web_url": "https://developers.kakao.com/mobile"
#                         }
#                     }
#                 ],
#                 "address": "서울 중구 퇴계로 166",
#                 "address_title": "흥국빌딩 2층 아시아경제 교육센터"
#             })
#         }
#         response = requests.post(send_url, headers=headers, data=template)
#         response.status_code
#         backup_filename = glob.glob('D:/asdf/work/python/Chatbot-Yolov5/kakao_code.json.*')
#         os.remove(backup_filename)