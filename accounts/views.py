from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
import django.contrib.auth as account
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from main.models import Customer,Order

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main:index')
        else:
            messages.error(request,'You are not registered. Please register.')
            return redirect('accounts:register')
    else:
        if request.user.is_authenticated:
            return redirect('main:index')
        return render(request, 'account/login.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        if password1 == password2:
            if User.objects.filter(email = email).exists():
                messages.error(request,'Email Already Exists')
                return redirect('accounts:register')
            elif User.objects.filter(username = username).exists():
                messages.error(request,'Username Already Exists')
                return redirect('accounts:register')
            else:

                #sending email on successful registration
                stringed_template = render_to_string('email_template.html',{'name':username})

                mail = EmailMessage(
                    subject='Your Registration for Book World is successful',
                    body=stringed_template,
                    from_email=settings.EMAIL_HOST_USER,
                    to=[email],
                    
                )
                mail.fail_silently=False
                mail.send()

                #creating new user
                user = User.objects.create_user(username = username, password = password1, email = email)
                user.save()
                print('user created')
                
                #logging in new user created
                user = auth.authenticate(username=username, password=password1)
                auth.login(request, user)
                print('user logged in')

                #creating customer and order for new user registerd
                customer = Customer.objects.create(user=user,email=email)
                Order.objects.create(customer=customer)
                
                return redirect('main:index')
        else:
            messages.error(request,'Password not matching...')
            return redirect('accounts:register')
    else:
        if request.user.is_authenticated:
            return redirect('main:index')
        return render(request, 'account/signup.html')

def logout(request):
    print(request.user,"logged out")
    account.logout(request=request)
    return render(request, 'index.html')