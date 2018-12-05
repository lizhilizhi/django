from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def login(request):

    # f = open('templates/login.html','r',encoding='utf-8')
    # date =  f.read()
    # f.close()
    # return HttpResponse(date)
   # 获取用户提交方式
   # print(request.method)
   #   if request.method == "post":
   #      request.POST.get('user',None)
   #      request.POST.get('pwd',None)
   #      if user == 'root' and  pwd == '123':
    error_msg = ""
    if request.method == "POST":
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)
        if user == 'root' and pwd == "123":
            return  redirect('home')
        else:
            #用户名密码部匹配
            error_msg = "用户名密码不匹配"
    return  render(request,'login.html',{'error_msg':error_msg})

    return render(request,'login.html',{'error_message':'error_message'})

USER_LIST =[
    {'username':'alex','email':'asasas',"gender":'男'}
]
for index in range(20):
    temp = {'username':'alex'+str(index),'email':'asasas',"gender":'男'}
    USER_LIST.append(temp)

# USER_LIST = [
#     {'id': 1, 'username': 'alex', 'email': 'asdfasdf', "gender": '男'},
#     {'id': 2, 'username': 'eriuc', 'email': 'asdfasdf', "gender": '男'},
#     {"id": 3,'username': 'seven', 'email': 'asdfasdf', "gender": '男'},
# ]

def home(request):
    # if request.method == "POST":
    if request.method =="GET":
        return render(request,'login.html')
    elif request.method == "POST":
        uu = request.POST.get('username')
        ee = request.POST.get('email')
        gg = request.POST.get('gender')
        temp = {'username':uu,'email':ee,"gender":gg}
        USER_LIST.append(temp)
    else:
            return render(request,'login.html')
    return render(request,'home.html',{'user_list':USER_LIST})