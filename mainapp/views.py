from django.shortcuts import render
from django.http import HttpResponse
from . import  models
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def Index(request):
   #return HttpResponse("all in one....")
   #menu7= Menu.objects.all()
   return render(request, 'index.html',{})

def WhatsappData(Ph,Message):
    import time
    import webbrowser as web
    import pyautogui as pg
    Phone = "+91" +Ph
    web.open('https://web.whatsapp.com/send?phone='+Phone+'&text='+Message)
    time.sleep(30)
    pg.press('enter')



def senddata(request):
    if request.method == "POST":
        Ph = request.POST['Phone']
        Message = request.POST['message']
        #print(ph,Message)
        WhatsappData(Ph,Message)
        msg="Message has successfully sent.."
        return render(request,"index.html",{'msg':msg})
    else:
        return HttpResponse("<h1>404 - Not Found :) </h1>")

def discover(request):
    
    if request.method == "POST":
        messages_name =request.POST.get('message-name', False);
        messages_email =request.POST.get('message-email', False);
        messages = request.POST.get('message', False);
        # send an email
        send_mail(
            messages_name,# subject
            messages, # message
            messages_email, # from email
            ['tmpdivya24@gmail.com'], # to email

        )

        return render(request,'discover.html',{'message_name': messages_name})
    else:
        return render(request,"discover.html", {})
    #return render(request,'discover.html')


def register(request):
    #if request.method == 'POST':
    #reg = Register.objects.all()
        
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def reg_done(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
      #  phone = request.POST['phone']
        password = request.POST['password']
        repeat_password = request.POST['repeat_password']
        if password == repeat_password:
            if User.objects.filter(username=username).exists():
                message.info(request,'Username Taken')
            elif User.objects.filter(email=email).exists():
                message.info(request,'Email Taken')
                

        user = User.objects.create_user(username = username, email = email, password=password)
        user.save();
        print('user created')
        return render (request, 'reg_done.html')

    else:
        return render (request, 'register.html')
'''
    regobj = models.Register()

    name = request.POST.get('name')
    mail = request.POST.get('mail')
    phone = request.POST.get('phone')
    psw = request.POST.get('psw')
    rpsw = request.POST.get('rpsw')
    #user=User.objects.create_user(name=name,psw=psw,mail=mail)
    #user.save()
    #print('user created')
    #return redirect('/')
    #all =[name, mail, phone, psw, rpsw]
 
    # for register
    regobj.name = name
    regobj.mail = mail
    regobj.phone = phone
    regobj.psw = psw
    regobj.pswr = rpsw
    regobj.save()

    return render(request, 'reg_done.html')
'''


def log_done(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

       
        return render(request, 'log_done.html')


    else:
        return render(request, 'sorry.html')
'''
    regobj = models.Register()
 
    lmail = request.POST.get('lmail')
    lpsw = request.POST.get('lpsw')
    
    
    # for register
    mail = regobj.mail
    psw = regobj.psw

    if lpsw != psw:
        return render(request, 'log_done.html')
    else:
        return render(request, 'sorry.html')
'''
#def sorry(request):
 #   return render(request,'sorry.html')

def send_mail_user(request):
    return render(request, 'send_mail_user.html')
'''
def index(request):
    if request.method == "POST":
        messages_name =request.POST['message-name']
        messages_email =request.POST['message-email']
        messages = request.POST['message']
        # send an email
        send_mail(
            message_name,# subject
            message, # message
            messages_email, # from email
            ['tmpdivya24@gmail.com'], # to email

        )

        return render(request, 'discover.html',{'message_name': messages_name})
    else:
        return render(request, "discover.html", {})


def send_mail(request):
    message=request.POST.get('message','')
    mail_id=request.POST.get('email','')
    email=EmailMessage(messages,EMAIL_HOST_USER,[mail_id])
    email.content_subtype='html'
    email.send()
    return HttpResponse("sent")
    return render(request,'send_mail.html')
'''