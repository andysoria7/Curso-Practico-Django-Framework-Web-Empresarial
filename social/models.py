from django.db import models

# Create your models here.

class Link(models.Model):
    key = models.SlugField(verbose_name="Nombre clave", max_length=100, unique=True) # Nos obligara a utilizar caracteres alfanumericos, guiones o barras y no nos permitira utilizar espacios ni caracteres especiales.
    name = models.CharField(verbose_name="Red social", max_length=200)
    url = models.URLField(verbose_name="Enlace", max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    
    class Meta:
        verbose_name = "enlace"
        verbose_name_plural = "enlaces"
        ordering = ['name'] # Se ordenen por fecha de creacion a la inversa.
    
    def __str__(self): # Devuelve el titulo del nombre.
        return self.name
    
