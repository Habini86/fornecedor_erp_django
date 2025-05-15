from django.db import models
from django.utils import timezone

class Fornecedor(models.Model):
    nome_razao = models.CharField("Nome/Razão Social", max_length=150)
    cnpj_cpf = models.CharField("CNPJ ou CPF", max_length=20)
    telefone = models.CharField("Telefone", max_length=20)
    email = models.EmailField("E-mail", max_length=100)
    endereco = models.CharField("Endereço", max_length=200)
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
    ]
    status = models.CharField("Status", max_length=10, choices=STATUS_CHOICES, default='ativo')

    def __str__(self):
        return self.nome_razao

class Compra(models.Model):
    descricao = models.CharField("Descrição", max_length=200)
    data = models.DateTimeField("Data da compra", default=timezone.now)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.descricao} - {self.fornecedor.nome_razao} - {self.data.strftime('%d/%m/%Y')}"