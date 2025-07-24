from django.shortcuts import render



# Create your views here.
#welcome message
from django.http import HttpResponse

def index(request): return HttpResponse("Welcome to my book store.")

# customuser
from django.contrib.auth import get_user_model
User = get_user_model()
user = User.objects.get(id=1)
