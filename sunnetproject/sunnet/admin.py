import decimal

from django.contrib import admin
from .models import GELEN_TAKILAR, KISILER, TAKI_TURU
from django.template.defaultfilters import floatformat
from django.utils.html import format_html


# Register your models here.


@admin.display(description='Adı Soyadı')
def upper_case_name(obj):
    return ("%s %s" % (obj.AD, obj.SOYAD)).upper()


@admin.display(description='MIKTAR')
def float_miktar(obj):
    return format_html('<b>{}</b>', floatformat(obj.MIKTAR, -2))

class GELEN_TAKILAR_Admin(admin.ModelAdmin):
    list_display = ("id",upper_case_name, 'ACIKLAMA', float_miktar,'KISI','TAKI_TUR')
    list_filter = ('TAKI_TUR', 'KISI','MIKTAR')
    search_fields = ("id", 'AD', 'SOYAD', 'ACIKLAMA', 'MIKTAR')
    ordering = ('id', 'AD', 'SOYAD', 'ACIKLAMA', 'MIKTAR')
    list_per_page = 10
    list_display_links = (upper_case_name,)
    # list_editable = ('MIKTAR','KISI','TAKI_TUR')


admin.site.register(GELEN_TAKILAR, GELEN_TAKILAR_Admin)
admin.site.register(KISILER)
admin.site.register(TAKI_TURU)
