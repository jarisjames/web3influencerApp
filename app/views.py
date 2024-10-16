from django.shortcuts import render

def home(request):
    return render(request, 'app/home.html')
from django.shortcuts import render

def merch(request):
    return render(request, 'app/merch.html')  # Adjusted to include the 'app' directory

