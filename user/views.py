from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import UserCar
from car.models import Car, Brand
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login , update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def sign(request):
    if request.method == 'POST':
        reg_form = forms.Reg(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            return redirect('sign')
    
    else:
        reg_form = forms.Reg()
    return render(request, 'sign.html', {'form' : reg_form})


def loginn(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['username']
            pas = form.cleaned_data['password']
            user = authenticate(username = name, password = pas)

            if user is not None:
                login(request, user)
                return redirect('pro')
            else:
                return redirect('log')
        else:    
            return render(request, 'log.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'log.html', {'form' : form})
    

def profile(request):
    profile_form = forms.Change_usr(instance=request.user)
    purchased_cars = UserCar.objects.filter(user=request.user)
    return render(request, 'pro.html', {'form': profile_form, 'purchased_cars': purchased_cars})


def logoutt(request):
    logout(request)
    return redirect('show_car')


def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.Change_usr(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('pro')
    else:
        profile_form = forms.Change_usr(instance = request.user)
    return render(request, 'edit.html', {'form' : profile_form})


def buy_car(request, id):
    carr = get_object_or_404(Car, pk=id)
    UserCar.objects.create(user=request.user, car=carr)

    if carr.car_quantity > 0:
        carr.car_quantity -= 1
        carr.save()
        return redirect('pro')
    else:
        messages.error(request, "Sorry, this car is not available.")
        return redirect('vd', id=id)