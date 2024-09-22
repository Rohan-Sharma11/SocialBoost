from django.shortcuts import render, redirect
from .forms import FollowForm,LikeForm,CommentForm
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm
from django.contrib.auth.decorators import login_required


# Create your views here.



#Signup view
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})





# Login view
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid credentials')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})






#--------------------------------------------------

def BotRequestView(request):
    if request.method == 'POST':
        form = FollowForm(request.POST)
        form.request_type = "follow"
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        return render(request, 'follow_page.html', context={'form':FollowForm()})
    return render(request, 'follow_page.html', context={'form':FollowForm()})


def BotLikeView(request):
    if request.method == 'POST':
        form = LikeForm(request.POST)
        form.request_type = "like"
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        return render(request, 'like_page.html', context={'form':LikeForm()})
    return render(request, 'like_page.html')




def BotCommentView(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        form.request_type = "comment"
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        return render(request, 'comment_page.html', context={'form':CommentForm()})
    return render(request, 'comment_page.html', context={'form':CommentForm()})

def SuccessView(request):
    return render(request,'success.html')


def HomeView(request):
    return render(request, 'home.html')
