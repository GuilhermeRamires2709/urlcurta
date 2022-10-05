from django.db import models
import random
from .utils import gerador_codigo
# Create your models here.
class URL(models.Model):

        def save(self, *args, **kwargs):
            print("save foi executado")
            if self.shortcode is None or self.shortcode == "":
                # mesmo que: if self.shortcode in (None,""):
                self.shortcode = gerador_codigo()
            super(URL, self).save(*args, **kwargs)
        # cria campo url, do tipo CharField, tamanho máximo 220:
        url = models.CharField(max_length=220)
        #cria campo shortcode, tamanho máximo 15
        shortcode = models.CharField(max_length=15, unique=True, blank=True)
        #campos autoincriment para data de atualização + criação
        atualizado = models.DateTimeField(auto_now=True)
        criado = models.DateTimeField(auto_now_add=True)
        # método que retorna string com identificação do objeto

        def __str__(self):
            return str(self.url)

