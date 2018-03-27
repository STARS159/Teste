from django.contrib import admin
from .models import (Pessoa,EventoCientifico,Autor,PessoaJuridica,PessoaFisica,Evento,ArtigoCientifico) 
# Register your models here.

admin.site.register(Pessoa)
admin.site.register(EventoCientifico)
admin.site.register(Autor)
admin.site.register(PessoaJuridica)
admin.site.register(PessoaFisica)
admin.site.register(Evento)
admin.site.register(ArtigoCientifico)