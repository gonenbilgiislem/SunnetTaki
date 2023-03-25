from django.contrib import admin

from .models import GELEN_TAKILAR, KISILER, TAKI_TURU


# Register your models here.


@admin.display(description='Adı Soyadı')
def upper_case_name(obj):
    return ("%s %s" % (obj.AD, obj.SOYAD)).upper()

class GELEN_TAKILAR_Admin(admin.ModelAdmin):
    list_display = ("id",upper_case_name, 'ACIKLAMA', 'MIKTAR','KISI','TAKI_TUR')
    list_filter = ('TAKI_TUR', 'KISI','MIKTAR')
    search_fields = ("id", 'AD', 'SOYAD', 'ACIKLAMA', 'MIKTAR')
    ordering = ('id', 'AD', 'SOYAD', 'ACIKLAMA', 'MIKTAR')
    list_per_page = 1000

admin.site.register(GELEN_TAKILAR, GELEN_TAKILAR_Admin)
admin.site.register(KISILER)
admin.site.register(TAKI_TURU)
