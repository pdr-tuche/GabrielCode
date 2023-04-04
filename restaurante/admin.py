from django.contrib import admin
from .models import Funcionario, Endereco


class FuncionarioAdmin(admin.ModelAdmin):
    fields = ('nome', 'cpf', 'telefone', 'area', 'endereco' )

class EnderecoAdmin(admin.ModelAdmin):
    fields = ('cep', 'rua', 'numero', 'complemento')





admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)

