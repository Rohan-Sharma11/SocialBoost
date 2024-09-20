from django.db import models

# Create your models here.

class InstaUser(models.Model):
    email_id = models.EmailField()




class BotRequest(models.Model):
    request_type = models.CharField(max_length=10)

