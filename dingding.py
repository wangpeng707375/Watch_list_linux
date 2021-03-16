import requests
import json
import schedule
import time
from Watch_list import get_data
from Watch_list import write_data
def send_msg():
        headers = {'Content-Type': 'application/json;charset=utf-8'}
        url = 'https://oapi.dingtalk.com/robot/send?access_token=605e04951eaeef4c1297b68f0eb85a19596c3c9f53eb7a8ac6cbd90d3398c27c'
        json_text = {
            "msgtype": "text",
            "text": {
            "content":get_data.mailWrite()
            }
        }
        write_data.write_excel()
        return requests.post(url, json.dumps(json_text), headers=headers).content

if __name__ == '__main__':
     # schedule.every(1).minutes.do(send_msg)
     schedule.every().monday.at("08:30").do(send_msg)  # 部署每个星期一执行job()函数的任务
     while True:
         schedule.run_pending()
         time.sleep(1)


