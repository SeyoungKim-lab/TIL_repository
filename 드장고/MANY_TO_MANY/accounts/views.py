from django.shortcuts import render, redirect
# 로그인 폼 임포트, 비밀번호변경 폼 임포트
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
# 입력받은 정보기반으로 로그인하여 세션 생성하는 login함수 임포트
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# 커스텀 회원가입폼 임포트
from .forms import CustomUserCreationForm
# login_required
from django.contrib.auth.decorators import login_required
# 회원정보 수정
from .forms import CustomUserChangeForm
# 비밀번호 변경 시 세션 무효화를 막아주는 함수
from django.contrib.auth import update_session_auth_hash
# 유저모델 직접 임포트 하지 않고 get_user_model 함수 사용
from django.contrib.auth import get_user_model


# Create your views here.
def login(request):
    # 만약 로그인된 사용자면, 로그인 기능자체를 막는다
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')

#회원가입
def signup(request):
    # 만약 로그인된 사용자면, 회원가입 기능자체를 막는다
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)

# 회원탈퇴
@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('articles:index')

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form
    }
    return render(request, 'accounts/password.html', context)




def profile(request,username):
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {
        'person' : person,
    }
    return render(request, 'accounts/profile.html', context)


@login_required
def follow(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    
    # 게시글작성자와 로그인한사람이 다른경우(즉, 팔로우 가능)
    if person != request.user:
        # 게시글작성자의 팔로워목록에 이미 로그인사용자가 있다면
        if request.user in person.followers.all():
            # 팔로우 취소
            person.followers.remove(request.user)
        else:   # 없다면 팔로우
            person.followers.add(request.user)
    return redirect('accounts:profile', person.username)