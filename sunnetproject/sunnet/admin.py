from django.contrib import admin
from .models import GELEN_TAKILAR, KISILER, TAKI_TURU

# Register your models here.
class GELEN_TAKILAR_Admin(admin.ModelAdmin):
    list_display = ('AD', 'SOYAD', 'ACIKLAMA', 'MIKTAR','KISI','TAKI_TUR')
    list_filter = ('AD', 'SOYAD', 'ACIKLAMA', 'MIKTAR')

admin.site.register(GELEN_TAKILAR, GELEN_TAKILAR_Admin)
admin.site.register(KISILER)
admin.site.register(TAKI_TURU)