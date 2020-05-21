from django import forms
from captcha.fields import CaptchaField

class YourForm(forms.Form):
    captcha = CaptchaField()