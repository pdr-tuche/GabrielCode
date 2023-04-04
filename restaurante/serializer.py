from rest_framework import serializers
from .models import Funcionario, Endereco


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'

class FuncionarioSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    class Meta:
        model = Funcionario
        fields = '__all__'


