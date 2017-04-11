import datetime

from django.http import JsonResponse
from django.shortcuts import render, render_to_response
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

flag=1
def sayHello(request):
    return  render(request,"index.html",locals())

def blank(request):
    return render(request,"blank.html",locals())

def tables(requst):
    return render(requst,"tables.html",locals())

def flot(request):
    return render(request,'flot.html',locals())

@csrf_exempt
def AjaxTable(request):
    global flag
    print('ok!====================================================')
    data=[]
    temp = {'number':305,'state':"开",'temp':35,'speed':5,'fee':15,}
    data.append(temp)
    temp = {'number':306, 'state':"开", 'temp':20, 'speed':4, 'fee':18, }
    data.append(temp)
    temp = {'number':307, 'state':'开', 'temp':15, 'speed':2, 'fee':20, }
    data.append(temp)
    res = {'rooms': data,"flag":flag,'lim':flag}
    flag+=1
    return JsonResponse(res)

@csrf_exempt
def renew(request):
    print('进入函数!')
    if request.method== "GET":
        print("get方式无法更新数据！")
        #return JsonResponse({})
        return render(request, 'buttons.html', locals())

    elif request.method== "POST":
        try:
            key=request.POST["key"]
        except:
            key=None

        if key!="ok":
            print("验证错误！")
        else:
            print("成功！")
            datalist=request.POST['data']
            print(datalist)
            for item in datalist:
                print(item)
                #print(datalist[item])
            return render(request,'buttons.html',locals())


