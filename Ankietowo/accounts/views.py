from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.urls import reverse


@login_required
def profile(request):
    created = request.GET.get("created", False)
    return render(request, "accounts/profile.html", {"created": created})


def logout_view(request):
    logout(request)
    return redirect("login")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse("accounts:profile") + "?created=True")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})
