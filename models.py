#coding=utf8

from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=250, help_text = "Título para humanos de la categoría.")
    slug = models.SlugField(unique=True, help_text="Usa letras, número y underscores. De aquí sale la URL.")
    description = models.TextField(help_text="Descripción de la categoría.")
    
    class Admin:
        pass
    
    def __unicode__(self):
        return self.title