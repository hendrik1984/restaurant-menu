from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
  template_name = "users/login.html"

  def form_valid(self, form):
    messages.success(self.request, f"Welcome Back, {form.get_user().username}!")
    return super().form_valid(form)

# Create your views here.
def signup(request):
  if request.method == "POST":
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      messages.success(request, f"Welcome, {user.username}")
      return redirect("dashboard")
  else:
    form = CustomUserCreationForm()

  return render(request, "users/signup.html", {"form": form})

@login_required
def dashboard(request):
  return render(request, "users/dashboard.html")


