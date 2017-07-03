import datetime

from django.http import JsonResponse
from django.shortcuts import render, render_to_response
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from web_project import Pdata

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
    temp = {'number':Pdata.Pdata['00'],'state':Pdata.Pdata['01'],'Ptemp':Pdata.Pdata['02'],'Ntemp':Pdata.Pdata['03'],'speed':Pdata.Pdata['04'],'fee':Pdata.Pdata['05'],}
    data.append(temp)
    temp = {'number':Pdata.Pdata['10'],'state': Pdata.Pdata['11'], 'Ptemp': Pdata.Pdata['12'], 'Ntemp': Pdata.Pdata['13'], 'speed': Pdata.Pdata['14'],'fee': Pdata.Pdata['15'],}
    data.append(temp)
    temp = {'number': Pdata.Pdata['20'], 'state': Pdata.Pdata['21'], 'Ptemp': Pdata.Pdata['22'], 'Ntemp': Pdata.Pdata['23'], 'speed': Pdata.Pdata['24'],'fee': Pdata.Pdata['25'],}
    data.append(temp)
    temp = {'number': Pdata.Pdata['30'], 'state': Pdata.Pdata['31'], 'Ptemp': Pdata.Pdata['32'], 'Ntemp': Pdata.Pdata['33'], 'speed': Pdata.Pdata['34'],'fee': Pdata.Pdata['35'],}
    data.append(temp)
    res = {'rooms': data,"flag":Pdata.Pdata['roomS'],'lim':Pdata.Pdata['roomN']}
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
            Pdata.Pdata['roomN']=request.POST['roomN']
            Pdata.Pdata['roomS']=request.POST['roomS']
            for m in range(0,4):
                for n in range(0,6):
                    Pdata.Pdata["%d%d"%(m,n)]=request.POST["%d%d"%(m,n)]

            # datalist=request.POST['data']
            # print(datalist)
            # for item in datalist:
            #     print(datalist[item])
            #     #print(datalist[item])
            return render(request,'buttons.html',locals())


