from django.http import request
from django.shortcuts import render

# Create your views here.


def index(self):
    return render(request, template_name='index.html')