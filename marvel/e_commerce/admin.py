from django.contrib import admin

# NOTE: Tenemos que importar los modelos con los que vamos a trabajar:
from e_commerce.models import *

# Register your models here.

# NOTE: Aquí personalizamos los campos en el Django Admin.

@admin.register(Comic)
class ComicsAdmin(admin.ModelAdmin):
    # NOTE: Para seleccionar los campos en la tabla de registros
    list_display = ('marvel_id', 'title', 'stock_qty', 'price')

    # NOTE: Filtro lateral de elementos:
    list_filter= ('marvel_id','title')
    
    # NOTE: Buscador de elementos en la columna:
    search_fields = ['title']

    # NOTE: Para seleccionar los campos en el registro. 
    fields = ('marvel_id', 'title', 'stock_qty')

    # NOTE: Genera un campo desplegable con los registros seleccionados.
    # fieldsets = (
    #     (None, {
    #         'fields': ('marvel_id', 'title', 'stock_qty')
    #     }),
    #     ('Advanced options', {
    #         'classes': ('collapse',),
    #         'fields': ('description','price', 'picture'),
    #     }),
    # )
    pass

@admin.register(Wish_list)
class Wisht_listsAdmin(admin.ModelAdmin):
    # NOTE: Para seleccionar los campos en la tabla de registros
    list_display = ('id', 'user_id', 'comic_id', 'favorite', 'cart', 'wished_qty','buyed_qty')

    # NOTE: Filtro lateral de elementos:
    list_filter= ('id','user_id')
        
    # NOTE: Filtro lateral de elementos:
    list_filter= ('id','user_id', 'comic_id')
        
    # NOTE: Buscador de elementos en la columna:
    search_fields = ['title']
    
    # NOTE: Buscador de elementos en la columna:
    #search_fields = ['favorite']

    # NOTE: Buscador de elementos en la columna:
    #search_fields = ['cart']    

    # NOTE: Buscador de elementos en la columna:
    #search_fields = ['wished_qty']

    # NOTE: Buscador de elementos en la columna:
    #search_fields = ['buyed_qty']

    # NOTE: Para seleccionar los campos en el registro. 
    fields = ('user_id', 'comic_id', 'favorite', 'cart', 'wished_qty', 'buyed_qty')

    # NOTE: Genera un campo desplegable con los registros seleccionados.
    #fieldsets = (
    #     (None, {
    #         'fields': ('marvel_id', 'title', 'stock_qty')
    #     }),
    #     ('Advanced options', {
    #         'classes': ('collapse',),
    #         'fields': ('description','price', 'picture'),
    #     }),
    # )
    # NOTE: puede definirse fields o fieldsets (NO AMBOS)
    pass