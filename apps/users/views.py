from django.shortcuts import render
from django.views.generic import TemplateView,View
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from .models import UserProfile
from .forms import LoginForm
# Create your views here.
#首页
class IndexView(TemplateView):
    template_name = 'index.html'
#支持邮箱登录
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    def get(self,request):
        return render(request,'login.html',{})
    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST['username']
            pass_word = request.POST['password']
            user = authenticate(request, username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return render(request, 'index.html', {})
            else:
                return render(request, 'login.html', {'msg': '用户名或者密码错误！'})
        else:
            return render(request,'login.html',{'login_form':login_form})
# class LoginView(TemplateView):
#     template_name = 'login.html'
# #注册
class RegisterView(TemplateView):
    template_name = 'register.html'


