from rest_framework import viewsets
from .serializer import FuncionarioSerializer, EnderecoSerializer
from .models import Funcionario, Endereco

class FuncionarioViewSet(viewsets.ModelViewSet):
    serializer_class = FuncionarioSerializer
    queryset = Funcionario.objects.all()


class EnderecoViewSet(viewsets.ModelViewSet):
    serializer_class = EnderecoSerializer
    queryset = Endereco.objects.all()