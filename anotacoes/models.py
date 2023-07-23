from django.db import models

class anotacao(models.Model):
    nome = models.CharField(max_length=100, null=False)
    fotos = models.TextField(null=False)
    observacao = models.TextField(null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
      verbose_name_plural = 'Anotações'

    def __str__(self):
      return self.nome
    

class devendo(models.Model):
    pessoa = models.ForeignKey(anotacao, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=7,decimal_places=2)

    class Meta:
      verbose_name_plural = 'Devedores'

    def __str__(self) -> str:
       return self.pessoa


