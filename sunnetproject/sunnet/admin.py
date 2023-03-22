from django.contrib import admin
from .models import GELEN_TAKILAR, KISILER, TAKI_TURU

# Register your models here.
class GELEN_TAKILARAdmin(admin.ModelAdmin):
    list_display = ('ID', 'AD', 'SOYAD', 'ACIKLAMA', 'MIKTAR', 'TAKI_TUR_ID', 'KISI_ID')
    list_filter = ('ID', 'AD', 'SOYAD', 'ACIKLAMA', 'MIKTAR', 'TAKI_TUR_ID', 'KISI_ID')

class KISILERAdmin(admin.ModelAdmin):
    list_display = ('ID', 'AD')
    list_filter = ('ID', 'AD')

class TAKI_TURUAdmin(admin.ModelAdmin):
    list_display = ('ID', 'AD')
    list_filter = ('ID', 'AD')



admin.site.register(GELEN_TAKILAR, GELEN_TAKILARAdmin)
admin.site.register(KISILER, KISILERAdmin)
admin.site.register(TAKI_TURU, TAKI_TURUAdmin)