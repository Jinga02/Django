from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login # login
from django.contrib.auth import logout as auth_logout # logout


# Create your views here.
def login(request):
    if request.method == 'POST':
        #로그인 처리를 해준다.
        form = AuthenticationForm(request, request.POST) # 유저가 입력한 form이 채워진다.
        if form.is_valid():
            auth_login(request, form.get_user()) # 2번째 인자 = 어떤 유저를 로그인할건지
            return redirect('articles:index')
    else:
        # 비어있는 로그인 페이지를 제공
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)    # django에서 기본으로 logout 할 수 있게 지원
    return redirect('articles:index')


