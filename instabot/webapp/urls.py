
from django.contrib import admin
from django.urls import path
from webapp import views
from webapp.views import InstaRegistrationForm, BotRequestProfileView, HomeView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.HomeView, name = 'home'),
    path('register/',views.InstaRegistrationView,name ='register'),
    path('bot_request/',views.BotRequestProfileView,name='bot_request'),
]
