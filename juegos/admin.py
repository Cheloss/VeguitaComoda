# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from juegos.models import Category, Noticia, Foto, JuegosInflables
from sorl.thumbnail.admin import AdminImageMixin

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('name','category','sort_order','id')
    list_filter = ('created',)
    list_search = ('name',)
class JuegosAdmin(admin.ModelAdmin):
    list_display = ('name','category','sort_order','id')
    list_filter = ('created',)
    list_search = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    pass
class FotoAdmin(AdminImageMixin, admin.ModelAdmin):
    pass

admin.site.register(Category,CategoryAdmin)
admin.site.register(Noticia,NoticiaAdmin)
admin.site.register(Foto,FotoAdmin)
admin.site.register(JuegosInflables,JuegosAdmin)