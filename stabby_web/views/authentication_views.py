from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import redirect, render
from stabby_web.enums import Module


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")

    form = AuthenticationForm()

    return render(
        request=request, template_name="stabby_web/login.html", context={"form": form}
    )


def logout_view(request):
    logout(request)

    form = AuthenticationForm()

    return render(
        request=request, template_name="stabby_web/login.html", context={"form": form}
    )
