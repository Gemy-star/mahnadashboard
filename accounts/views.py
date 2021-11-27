from django.contrib import messages, auth
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View

from .models import User


class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']

        if email and password:
            exis = User.objects.filter(email=email).exists()
            user = auth.authenticate(email=email, password=password)
            if user:
                if user.is_active:
                    auth.login(request, user)
                    email = User.objects.get(email=email).email

                    email_subject = 'You Logged into your Portal account'
                    email_body = "If you think someone else logged in. Please contact support or reset your password.\n\nYou are receving this message because you have enabled login email notifications in portal settings. If you don't want to recieve such emails in future please turn the login email notifications off in settings."
                    fromEmail = 'noreply@exam.com'
                    email = EmailMessage(
                        email_subject,
                        email_body,
                        fromEmail,
                        [email],
                    )
                    messages.success(request, "Welcome, " + user.email + ". You are now logged in.")

                    return redirect('home-page')

            else:
                user_n = User.objects.filter(email=email).exists()
                if user_n:
                    user_v = User.objects.get(email=email)
                    if user_v.is_active:
                        messages.error(request, 'من فضلك تأكد من صحة البيانات')
                        return render(request, 'accounts/login.html')
                    else:
                        messages.error(request, 'من فضلك تأكد من صحة البيانات')
                        return render(request, 'accounts/login.html')

        messages.error(request, 'من فضلك تأكد من صحة البيانات')
        return render(request, 'accounts/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


class RegisterManager(View):
    login_required = True
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user = User.objects.create_manager(email=email, first_name=first_name, last_name=last_name,
                                           address=address, password=password, phone=phone)
        if user is not None:
            login(request, user)
            return redirect('home-page')

    def get(self, request):
        context = {}
        return render(request, 'accounts/register_manager.html', context)


class EmployeeControl(View):
    login_required = True
    def get(self, request):
        context = {"employees": User.objects.exclude(user_type=1)}
        return render(request, 'accounts/employee-control.html', context=context)


class RegisterAccountant(View):
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user = User.objects.create_accountant(email=email, first_name=first_name, last_name=last_name,
                                              address=address, password=password, phone=phone)
        if user is not None:
            login(request, user)
            return redirect('home-page')

    def get(self, request):
        context = {}
        return render(request, 'accounts/register-accountant.html', context)


class RegisterResident(View):
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user = User.objects.create_resident(email=email, first_name=first_name, last_name=last_name,
                                            address=address, password=password, phone=phone)
        if user is not None:
            login(request, user)
            return redirect('home-page')

    def get(self, request):
        context = {}
        return render(request, 'accounts/register-resident.html', context)



class RegisterEntry(View):
    login_required = True
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user = User.objects.create_entry(email=email, first_name=first_name, last_name=last_name,
                                           address=address, password=password, phone=phone)
        if user is not None:
            login(request, user)
            return redirect('home-page')

    def get(self, request):
        context = {}
        return render(request, 'accounts/register-entry.html', context)




class RegisterPreview(View):
    login_required = True
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user = User.objects.create_preview(email=email, first_name=first_name, last_name=last_name,
                                           address=address, password=password, phone=phone)
        if user is not None:
            login(request, user)
            return redirect('home-page')

    def get(self, request):
        context = {}
        return render(request, 'accounts/register-preview.html', context)