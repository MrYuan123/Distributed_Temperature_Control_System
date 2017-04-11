import time
import urllib

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
        send_data['data']={'1':('1','2','3','4','5'),'2':('9','8','7','6','5')}
        #send_data['1']=(str(num1),'开','35','6')
        #send_data['2']=(str(num2),'开',"25",'8')
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