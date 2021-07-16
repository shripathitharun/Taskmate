from django.shortcuts import render,redirect
from .forms import CustomRegisterForm
from django.contrib import messages

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send(tomail,name):
    from_add='chowdary8551@gmail.com'
    to_add=tomail
    subject="Registration Successful!!"

    msg=MIMEMultipart()
    msg['From']=from_add
    msg['To']=to_add
    msg['Subject']=subject

    body="<b>Dear "+name+", You have successfully registered on taskmate.Now Login and access your own Taskmate</b>"
    msg.attach(MIMEText(body,'html'))


    message=msg.as_string()

    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(from_add,'cifvjezlszfpfpkc')
    server.sendmail(from_add,to_add,message)
    server.quit()
def register(request):
    if request.method=="POST":
        register_form=CustomRegisterForm(request.POST)
        if register_form.is_valid():
            str=request.POST["email"]
            name=request.POST["username"]
            register_form.save()
            send(str,name)
            messages.success(request,("New user account created!! Login to get started"))
            return redirect('register')

    else:
        register_form=CustomRegisterForm()
    return render(request,'register.html',{'register_form' : register_form})
