
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    #path('', views.enterAadhar, name="enterAadhar"),
    #url('enterotp', views.enterOTP, name="enterotp"),
    path('', views.inputAadhaar, name="input_aadhaar"),
    path('validate_aadhaar', views.validateAadhaar, name="validate_aadhaar"),
    path('validate_otp', views.validateOTP, name="validate_otp")
]



