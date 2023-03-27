import decimal

from django.contrib import admin
from .models import GELEN_TAKILAR, KISILER, TAKI_TURU
from django.template.defaultfilters import floatformat
from django.utils.html import format_html


# Register your models here.


@admin.display(description='Adı Soyadı', ordering='AD')
def soyad_buyuk_harf(obj):
    if obj.SOYAD is None:
        return str(obj.AD)
    else:
        return f'{obj.AD} {obj.SOYAD.upper()}'


@admin.display(description='MIKTAR')
def float_miktar(obj):
    return format_html('<b>{}</b>', floatformat(obj.MIKTAR, -2))


class GELEN_TAKILAR_Admin(admin.ModelAdmin):
    list_display = ("id",soyad_buyuk_harf, 'ACIKLAMA', float_miktar,'KISI','TAKI_TUR')
    list_filter = ('TAKI_TUR', 'KISI','MIKTAR')
    search_fields = ("id", 'AD', 'SOYAD', 'ACIKLAMA', 'MIKTAR')
    ordering = ('id',  'ACIKLAMA', 'MIKTAR', 'TAKI_TUR', 'KISI')
    list_per_page = 10
    list_display_links = (soyad_buyuk_harf,)
    # list_editable = ('MIKTAR','KISI','TAKI_TUR')


admin.site.register(GELEN_TAKILAR, GELEN_TAKILAR_Admin)
admin.site.register(KISILER)
admin.site.register(TAKI_TURU)
