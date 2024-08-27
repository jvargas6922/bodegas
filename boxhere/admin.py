from django.contrib import admin
from .models import BodegaTipo, Bodega, Noticia, Like

# Register your models here.

admin.site.register(BodegaTipo)
admin.site.register(Bodega)
admin.site.register(Noticia)
admin.site.register(Like)