from django.contrib import admin
from .models import GELEN_TAKILAR, KISILER, TAKI_TURU

# Register your models here.
class GELEN_TAKILARAdmin(admin.ModelAdmin):
    list_display = ('AD', 'SOYAD', 'ACIKLAMA', 'MIKTAR')
    list_filter = ('AD', 'SOYAD', 'ACIKLAMA', 'MIKTAR')

admin.site.register(GELEN_TAKILAR, GELEN_TAKILARAdmin)
admin.site.register(KISILER)
admin.site.register(TAKI_TURU)