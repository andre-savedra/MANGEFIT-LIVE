from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class AdminCustomUser(UserAdmin):
    model = CustomUser
    list_display = ['id','email','cpf','is_active']
    list_display_links = ('id','email','cpf','is_active',)
    fieldsets = (
        (None, {'fields':('email','password')}),
        ('Permissões', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions',)}),
        ('Gerenciamento', {'fields': ('last_login',)}),
        ('Cadastro', {'fields': ('cpf', 'telefone',)}),
        ('Endereço', {'fields': ('rua', 'cep', 'bairro', 'cidade', 'estado',)}),
    )
    filter_horizontal = ('groups', 'user_permissions',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'groups', 'user_permissions',)
        }),
    )
    search_fields = ['email','cpf',]
    ordering = ['email']

admin.site.register(CustomUser,AdminCustomUser)

admin.site.register(Ingrediente)
admin.site.register(Salada)
admin.site.register(Salada_Avaliacao)
admin.site.register(Pedido)
admin.site.register(Item_Pedido)
