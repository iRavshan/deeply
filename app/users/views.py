from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserSignUpForm, UserSignInForm


def sign_up(request):
    context = {}
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            instance = form.save(commit=False)
            instance.username = email
            instance.save()
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                return redirect('home')
    context['form'] = UserSignUpForm() 
    return render(request, 'auth/signUp.html', context)



def sign_in(request):
    context = {}
    if request.method == 'POST':
        form = UserSignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    context['form'] = UserSignInForm()
    return render(request, 'auth/signIn.html', context)



@login_required
def log_out(request):
    logout(request)
    return redirect('signIn')