from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import SignupageForm, ContactForm, UpdateForm
from django.contrib import messages
from .models import Account
import csv
from django.http import HttpResponse


def loginpage(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Login successful.")
                return redirect("home")
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect("loginpage")

    else:
        form = AuthenticationForm()
        context = {"form": form}
        return render(request, "contacts_app/loginpage.html", context)


def signupage(request):
    if request.method == "POST":
        form = SignupageForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)
            messages.success(
                request, "Account created successfully. You are now logged in."
            )
            return redirect("loginpage")
        else:
            messages.error(
                request, "Error creating account. Please check the form and try again."
            )
    else:
        form = SignupageForm()
    context = {"form": form}
    return render(request, "contacts_app/signupage.html", context)


@login_required(login_url="loginpage")
def create_contact(request):
    if not request.user.is_authenticated:
        messages.error(request, "Please log in to access a contact.")
        return redirect("loginpage")
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            Account.objects.create(
                user=request.user,
                firstname=form.cleaned_data.get("firstname"),
                lastname=form.cleaned_data.get("lastname"),
                email=form.cleaned_data.get("email"),
                address=form.cleaned_data.get("address"),
                phoneNumber=form.cleaned_data.get("phoneNumber"),
                linkedin=form.cleaned_data.get("linkedin"),
                facebook=form.cleaned_data.get("facebook"),
                twitter=form.cleaned_data.get("twitter"),
            )
            messages.success(request, "Contact created successfully .")
            return redirect("home")

        else:
            messages.error(request, "Error creating contact")

    else:
        form = ContactForm()
    context = {"form": form}
    return render(request, "contacts_app/newcontact.html", context)


@login_required(login_url="loginpage")
def edit_contact(request, contact_id):
    if not request.user.is_authenticated:
        messages.error(request, "You are not authorized here.")
        return redirect("loginpage")

    contact = get_object_or_404(Account, id=contact_id, user=request.user)

    if request.method == "POST":
        form = UpdateForm(request.POST, instance=contact)

        if form.is_valid():
            form.save()
            messages.success(request, "Contact updated successfully.")
            return redirect("home")
        else:
            messages.error(request, "Error in the form. Please check again.")

    else:
        form = UpdateForm(instance=contact)

    context = {"form": form, "contact": contact}
    return render(request, "contacts_app/newcontact.html", context)


@login_required(login_url="loginpage")
def delete_contact(request, contact_id):
    if not request.user.is_authenticated:
        messages.error(request, "Please log in, to delete a contact.")
        return redirect("loginpage")

    contact = get_object_or_404(Account, id=contact_id, user=request.user)
    print("post delete")
    if request.method == "POST":
        print("delete")
        contact.delete()
        messages.success(request, "Contact deleted successfully.")
    return redirect("home")


@login_required(login_url="loginpage")
def home(request):
    user_contacts = Account.objects.filter(user=request.user).order_by(
        "firstname", "lastname"
    )
    return render(request, "contacts_app/home.html", {"user_contacts": user_contacts})


@login_required(login_url="loginpage")
def export__to_csv(request):
    user_contacts = Account.objects.filter(user=request.user).order_by(
        "firstname", "lastname"
    )

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="contacts.csv"'

    csv_writer = csv.writer(response)

    csv_writer.writerow(
        ["Name", "Email", "Phone Number", "LinkedIn", "Facebook", "Twitter"]
    )

    for contact in user_contacts:
        csv_writer.writerow(
            [
                f"{contact.firstname} {contact.lastname}",
                contact.email,
                contact.phoneNumber,
                contact.linkedin,
                contact.facebook,
                contact.twitter,
            ]
        )

    return response


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
