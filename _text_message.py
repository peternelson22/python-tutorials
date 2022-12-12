import time

import requests
import schedule


def send_text():
    try:
        resp = requests.post('https://textbelt.com/text', {
            'phone': '+447985103148',
            'message': 'Hello Jae',
            'key': 'textbelt',
        })
        print(resp.json())
    except Exception:
        print('somthing went wrong')


#schedule.every().day.at('08:00').do(send_text)
schedule.every(5).seconds.do(send_text)

while True:
    schedule.run_pending()
    time.sleep(1)