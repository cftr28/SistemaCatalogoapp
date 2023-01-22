from django.contrib import admin
from .models import Catalogo

# Register your models here.

class CatalogoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Catalogo, CatalogoAdmin)

