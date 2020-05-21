from django.shortcuts import render
from django.http import HttpResponse
from .models import DummyAadharData
import twilio
from twilio.rest import Client
import random
otp = 0
import requests
import json
#global send_otp
#send_otp = False
# Create your views here.


def inputAadhaar(request):
    return render(request,'index.html')


def validateAadhaar(request):
    #return HttpResponse('Enter aadhar')
    if request.method == 'POST':
        #print(request)
        user_aadhar = request.POST.get('aadharNo','')
        print(user_aadhar)
        length_of_aadhar = len(user_aadhar)
        print(length_of_aadhar)
        
        #recaptcha backend
        clientKey = request.POST['g-recaptcha-response']
        secretKey = 'Server side key'
        captchaData = {
            'secret' : secretKey,
            'response' : clientKey
        }
        #API URL
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data = captchaData)
        response = json.loads(r.text)
        verify = response['success']
        print('your success is ', verify)

        if length_of_aadhar == 12 and verify :
            present = DummyAadharData.objects.filter(aadhar_no = user_aadhar).exists()
            if present:
                user_phone = DummyAadharData.objects.filter(aadhar_no = user_aadhar)[0].mobile
                print(user_phone)
                print(present)
                #present = DummyAadharData.objects.filter(aadhar_no = user_aadhar).exists()
                #present = Entry.objects.filter(name='name', title='title').exists()
                generated_otp = random.randint(100000,999999)
                print(generated_otp)
                global otp
                otp = generated_otp
                account_sid = 'ACd308f731753a628b61548ea8dcdc50df'
                auth_token = '6e2bb6fb7c5b28dc138fb11bff5277ba'
                client = Client(account_sid, auth_token)
                message = client.messages.create(
                    body='OTP for your Aadhar card verification is - '+str(generated_otp),
                    from_='+12245151009',
                    to='+91'+str(user_phone)
                )
                print(message.sid)
                #global send_otp
                #send_otp = True
                return render(request, 'check_otp.html')
            else:
                return render(request, 'index.html', {"message":"Not a valid Aadhar Number. Please enter a Valid aadhar number"})
        else:
            print(verify)
            return render(request, 'index.html', {"message":"Please enter a Valid aadhar number", "verify":verify})

    #return render(request, 'index.html')    


def validateOTP(request):
    #return HttpResponse('Enter OTP')
    print(otp)
    print('hello')
    if request.method == 'POST':
        user_otp = request.POST.get('otp','')
        if user_otp == str(otp):
            return HttpResponse('Your verification process is Done.')
        else:
            return render(request, 'index.html', {"message":"Invalid OTP. Please Enter your aadhar no again for verification."})
    #return render(request, 'check_otp.html')
