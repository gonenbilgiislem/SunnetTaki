from django.shortcuts import render
from .models import GELEN_TAKILAR

from django.shortcuts import render
from .models import GELEN_TAKILAR


# Create your views here.
def index(request):
    context = {
        "ganimet": GELEN_TAKILAR.objects.all(),
        "head": {
            'id': "#",
            'AD': 'Adı',
            'SOYAD': 'Soyadı',
            'ACIKLAMA': 'Açıklama',
            'MIKTAR': 'Miktar',
            'TAKI_TUR': 'Ganimet Türü',
            'KISI': 'Kime Gelen Ganimet'
        }
    }
    return render(request, 'sunnet/index.html', {'icerik': context})


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
