from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('',views.HomeView, name = 'home'),
    path('follow/',views.BotRequestView, name = 'follow'),
    path('like/',views.BotLikeView, name = 'like'),
    path('comment/',views.BotCommentView, name = 'comment'),
    path('success/',views.SuccessView, name = 'success'),
    
]