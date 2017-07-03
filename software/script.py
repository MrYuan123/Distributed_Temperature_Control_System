import time
import urllib
import random
from requests import Request

postURL='http://127.0.0.1:8000/data/'
def script():

    num1=1
    num2=2
    while True:
        send_data={}
        Wtime = 4
        print("Wait time:%d second!" % Wtime)
        time.sleep(Wtime)

        send_data['key']='ok'
        for m in range(0,4):
            for n in range(0,6):
                send_data["%d%d"%(m,n)]=random.randint(0,100)

        send_data["roomN"]="3"
        send_data['roomS']='open'
        final_data=urllib.parse.urlencode(send_data).encode('utf-8')
        print(final_data)
        try:
            print("进入")
            req = urllib.request.Request(postURL,final_data)
            NowMachine = urllib.request.urlopen(req)
            print("结束！")
        except:
            print("未收到回复！")
        num1+=2
        num2+=3


script()