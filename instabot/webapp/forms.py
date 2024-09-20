from django import forms
from .models import InstaUser, BotRequest

class InstaRegistrationForm(forms.ModelForm):
    class Meta:
        model = InstaUser
        fields = ['email_id']


class BotRequestForm(forms.ModelForm):
    class Meta:
        model = BotRequest
        fields = ['request_type']