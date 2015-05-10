from django.contrib import admin

from .models import Wniosek, Przedmiot_Zamowienia

# Register your models here.

class Przedmiot_ZamowieniaAdmin(admin.ModelAdmin):
    class Meta:
        model = Przedmiot_Zamowienia

class WniosekAdmin(admin.ModelAdmin):
    class Meta:
        model = Wniosek
		
admin.site.register(Przedmiot_Zamowienia, Przedmiot_ZamowieniaAdmin)
admin.site.register(Wniosek, WniosekAdmin)