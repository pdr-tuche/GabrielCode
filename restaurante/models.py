from django.db import models

class Endereco(models.Model):
    cep = models.CharField(max_length=9)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=4)
    complemento = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return '%s, %s - %s' % (self.rua, self.numero, self.complemento)

class Funcionario(models.Model):

    AREA_FUNCIONARIO = (
        ('Atendimento','Atendimento' ),
        ('Cozinha','Cozinha'),
        ('Gerencia', 'Gerencia'),
        ('Pagamento', 'Pagamento'),
    )

    nome = models.CharField(blank=False, max_length=100)
    cpf = models.CharField()
    telefone = models.CharField()
    area = models.CharField(choices= AREA_FUNCIONARIO)
    endereco = models.ForeignKey(Endereco, related_name='endereco', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


