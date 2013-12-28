#coding=utf8

from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=250, help_text = "Ojo con la ortografía. Use mayúsculas adecuadamente según las normas del español.")
    slug = models.SlugField(unique=True, help_text="Usa letras, número y underscores. De aquí sale la URL.")
    description = models.TextField(help_text="Descripción de la categoría.")
    
    class Admin:
        pass
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __unicode__(self):
        return self.title