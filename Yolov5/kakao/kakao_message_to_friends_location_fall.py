# 친구에게 위치 템플릿으로 카톡보내기
# 낙상

import requests
import json
import os
import glob
from Yolov5.kakao import kakao_utils_friends
import sys



def send_message_to_friends_location_fall():
    KAKAO_TOKEN_FILENAME = "./kakao_code.json"  # "<kakao_token.json 파일이 있는 경로를 입력하세요.>"
    KAKAO_APP_KEY = "6188bf2cdc11ad8bb911d6ef9e0bcd46"
    tokens = kakao_utils_friends.update_tokens(KAKAO_APP_KEY, KAKAO_TOKEN_FILENAME)
    headers={"Authorization" : "Bearer " + tokens["access_token"]}

    friend_url = "https://kapi.kakao.com/v1/api/talk/friends"

    result = json.loads(requests.get(friend_url, headers=headers).text)

    friends_list = result.get("elements")

    for i in range(len(friends_list)):
        friend_id = friends_list[i].get("uuid")

        print(friend_id)
        send_url= "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"

        template={
            'receiver_uuids': '["{}"]'.format(friend_id),
            "template_object": json.dumps({
                "object_type": "location",
                "content": {
                    "title": "🆘 응급!! 낙상사고가 감지되었습니다!! 🆘",
                    "description": "🚑 낙상사고가 발생하였으니 119에 신고해주세요 🚑",
                    "image_url": "https://i.esdrop.com/d/f/NXl6YkfhTU/Kz1B5Qj0rB.png",
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
            })
        }
        response = requests.post(send_url, headers=headers, data=template)
        response.status_code
    backup_filename = glob.glob('D:/asdf/work/python/Chatbot-Yolov5/kakao_code.json.*')
    print(backup_filename)
    for f in backup_filename:
        os.remove(f)


if __name__ == '__main__':
    send_message_to_friends_location_fall()