from django.shortcuts import redirect, render
from .forms import signupForm,notesForm
from .models import signup
from django.contrib.auth import logout
from django.core.mail import send_mail
from BatchProject import settings
import requests
import json
import random

# Create your views here.

def index(request):
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            signupfrm=signupForm(request.POST)
            if signupfrm.is_valid():
                signupfrm.save()
                print("Signup Successfully!")

                #Send Mail
                sub="Re:Signup Successfully!"
                msg="Hello User, \nYour account has been created successfully! \nEnjoy our services. \n Thanks & Regards, \nBatchProject - TOPS Technologoies Pvt Ltd \n +91 9998506434 | sanketchauhanios@gmail.com"
                from_email=settings.EMAIL_HOST_USER
                #to_email=['shradhdhagvaghasiya83@gmail.com','raviyapayal17@gmail.com','gk.vekariya0@gmail.com','arjun7kagathara@gmail.com','bhagi.dudhrejiya2907@gmail.com']
                to_email=[request.POST['username']]

                send_mail(sub,msg,from_email,to_email)
                return redirect('notes')
            else:
                print(signupfrm.errors)
        elif request.POST.get('login')=='login':
            unm=request.POST['username']
            pas=request.POST['password']

            userid=signup.objects.get(username=unm)
            print("UserID:",userid.id)
            user=signup.objects.filter(username=unm,password=pas)
            if user:
                print("Login Successfully!")
                request.session['user']=unm
                request.session['userid']=userid.id

                '''# SMS Sending after Login!
                # mention url
                url = "https://www.fast2sms.com/dev/bulk"

                otp=random.randint(1111,9999)
                # create a dictionary
                my_data = {
                    # Your default Sender ID
                    'sender_id': 'FSTSMS', 
                    
                    # Put your message here!
                    'message': f'Hello User, \nYour account has been logged in successfully. \nYour one time password is {otp}', 
                    
                    'language': 'english',

                    'route': 'p',
                    
                    # You can send sms to multiple numbers
                    # separated by comma.
                    #'numbers': '7359333245,8347344100,9409702277,6353630122'    
                    'numbers': '8347344100,6353630122'   
                }
                
                # create a dictionary
                headers = {
                    'authorization': 'l9k8KiUuQ2mWLJ4vCVyasTO3z5XRDxeHIGrPgcFN6dB0nwbE1hk2KqzvN6THZQrEwRCdIm8cGj4ifbSn',
                    'Content-Type': "application/x-www-form-urlencoded",
                    'Cache-Control': "no-cache"
                }

                # make a post request
                response = requests.request("POST",
                                            url,
                                            data = my_data,
                                            headers = headers)
                #load json data from source
                returned_msg = json.loads(response.text)
                
                # print the send message
                print(returned_msg['message'])'''

                return redirect('notes')
            else:
                print("Error...Login Failed, Plz try again.")
        else:
            print("Somthing went wrong...Try again!")
    return render(request,'index.html')


def notes(request):
    user=request.session.get("user")
    if request.method=='POST':
        notefrm=notesForm(request.POST,request.FILES)
        if notefrm.is_valid():
            notefrm.save()
            print("Your notes has been uploaded!")
            return redirect('notes')
        else:
            print(notefrm.errors)
    else:
        notefrm=notesForm()
    return render(request,'notes.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect('/')

def updateprofile(request):
    user=request.session.get("user")
    userid=request.session.get("userid")
    if request.method=='POST':
        signupfrm=signupForm(request.POST)
        id=signup.objects.get(id=userid)
        if signupfrm.is_valid():
            signupfrm=signupForm(request.POST,instance=id)
            signupfrm.save()
            print("Your profile has been updated!")
            return redirect('notes')
        else:
            print(signupfrm.errors)
    else:
        signupfrm=signupForm()
    return render(request,'updateprofile.html',{'user':user,'userid':signup.objects.get(id=userid)})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
