import django_tables2 as tables
from django_tables2 import LazyPaginator

from .models import GELEN_TAKILAR


class GELEN_TAKILAR_Table(tables.Table):
    class Meta:
        model = GELEN_TAKILAR
        template_name = "django_tables2/bootstrap.html"
        fields = ("AD", 'SOYAD', 'ACIKLAMA', 'MIKTAR', 'TAKI_TUR', 'KISI')
