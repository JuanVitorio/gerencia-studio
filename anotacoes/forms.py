from django.forms import ModelForm
from .models import anotacao

class clienteForm(ModelForm):
  class Meta:
    model = anotacao
    fields = ['nome', 'fotos', 'observacao']