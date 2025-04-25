from django.contrib import messages
from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProfileUpdateForm, RegisterForm
from .models import Profile

User = get_user_model()


def register(request):
    """
    Handle user registration: display form, create new User,
    log them in, and redirect to home on success.
    """
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created.")
            return redirect("post_list")
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def profile_update(request):
    """
    Allow authenticated users to update their Profile (bio & avatar).
    """
    profile = request.user.profile
    form = ProfileUpdateForm(
        request.POST or None,
        request.FILES or None,
        instance=profile
    )
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Profile updated.")
        return redirect("profile", username=request.user.username)
    return render(request, "users/profile_edit.html", {"form": form})


def profile_detail(request, username):
    """
    Display a user's public profile by username.
    """
    user = get_object_or_404(User, username=username)
    return render(request, "users/profile.html", {"profile_user": user})
