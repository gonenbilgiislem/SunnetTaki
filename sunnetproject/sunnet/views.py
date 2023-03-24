from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import GELEN_TAKILAR, KISILER, TAKI_TURU
# Create your views here.
def index(request):
    ganimet = GELEN_TAKILAR.objects.all()
    return render(request, 'sunnet/index.html',{
        "ganimet": ganimet
    })


def about(request):
    return None


def contact(request):
    return None


def dashboard(request):
    return None


def login(request):
    return None


def register(request):
    return None


def logout(request):
    return None