from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth import authenticate, login 
from .forms import SignupageForm 
from django.contrib import messages

def loginpage(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('contactpage')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            return redirect('loginpage')

    else:
        form = AuthenticationForm()
        context = {"form": form}
        return render(request, 'contacts_app/loginpage.html', context)




def signupage(request):
    if request.method == 'POST':
        form = SignupageForm(request.POST)

        if form.is_valid():
            user = form.save()
     
            login(request, user)
            messages.success(request, 'Account created successfully. You are now logged in.')
            return redirect('loginpage')
        else:  
            messages.error(request, 'Error creating account. Please check the form and try again.')
    else:
        form = SignupageForm()

    context = {'form': form}
    return render(request, 'contacts_app/signupage.html', context)


def home(request) :
    return render(request,"contacts_app/home.html")



# def loginpage(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request=request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password")
#             user = authenticate(request, username=username, password=password)

#             if user is not None:
#                 login(request, user)
#                 messages.success(request, 'Login successful.')
#                 return redirect('contactpage')
#         else:
#             messages.error(request, 'Invalid username or password. Please try again.')
#             return redirect('loginpage')

#     else:
#         form = AuthenticationForm()
#         context = {"form": form}
#         return render(request, 'contacts_app/loginpage.html', context)

