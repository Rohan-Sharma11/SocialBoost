from django.contrib import admin
from .models import InstaUser, BotRequest

# Register your models here.

admin.site.register([
    InstaUser,
    BotRequest
])