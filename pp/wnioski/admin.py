from django.contrib import admin

from .models import Firma, Wniosek

# Register your models here.

class FirmaAdmin(admin.ModelAdmin):
    class Meta:
        model = Firma

class WniosekAdmin(admin.ModelAdmin):
    class Meta:
        model = Wniosek
		
admin.site.register(Firma, FirmaAdmin)
admin.site.register(Wniosek, WniosekAdmin)