from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    
class PessoaJuridica(models.Model):
    cnpj = models.CharField(max_length=100)
    razaoSocial = models.CharField(max_length=100)

class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length=100)


class Autor(Pessoa):
    curriculo = models.CharField(max_length=100)

class Evento(models.Model):
    nome = models.CharField(max_length=100)
    eventoPrincipal = models.CharField(max_length=100)
    sigla = models.CharField(max_length=100)
    dataEHoraDeInicio = models.DateTimeField(blank=True, null=True)
    palavrasChave = models.CharField(max_length=100)
    logotipo = models.CharField(max_length=100)
    realizador = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)

class EventoCientifico(Evento):
    issn = models.CharField(max_length=100)
    
class ArtigoCientifico(models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor)
    evento = models.OneToOneField(EventoCientifico, on_delete=models.CASCADE)

