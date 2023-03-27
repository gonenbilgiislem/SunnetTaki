from django.shortcuts import render
from .models import GELEN_TAKILAR, KISILER, TAKI_TURU


# Create your views here.
def home(request):
    return render(request, 'sunnet/home.html')


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

from django.views.generic import ListView
from django_tables2 import SingleTableView, LazyPaginator
from .tables import GELEN_TAKILAR_Table

class GELEN_TAKI_View(SingleTableView):
    model = GELEN_TAKILAR
    table_class = GELEN_TAKILAR_Table
    template_name = 'sunnet/people.html'
    paginate_by = 10
