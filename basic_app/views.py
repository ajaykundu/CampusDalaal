from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm



# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from basic_app.models import IntitutionModel,UserProfileInfo

# Create your views here.
def index(request):
    item = IntitutionModel.objects.all()
    nameofInst = 'hello'
    if request.user.is_authenticated() :
        nameofInst = UserProfileInfo.objects.get(user=request.user).slugInst
    return render(request,'basic_app/index.html',{'items':item,'instName':nameofInst})

@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basic_app/user_login/'
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save User Form to Database
            print('hello world')
            user = user_form.save(commit=False)
            user.is_active = False
            user.save()

            # # Hash the password
            # user.set_password(user.password)
            #
            # # Update with Hashed password
            # user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture
            # if 'profile_pic' in request.FILES:
            #     print('found it')
            #     # If yes, then grab it from the POST form reply
            #     profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()

            # Registration Successful!
            registered = True
            current_site = get_current_site(request)
            message = render_to_string('acc_active_email.html', {
                'user':user,
                'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_subject = 'Activate your blog account.'
            to_email = user_form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'basic_app/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):
    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("<h1>Please Confirm Your Email First!.</h1>")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("<h1>Invalid login details supplied.</h1>")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'basic_app/login.html', {})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
