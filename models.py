#coding=utf8
#modelos para Coltrane
import datetime
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from taggit.managers import TaggableManager

class Category(models.Model):
    title = models.CharField(max_length=250, help_text = "Ojo con la ortografía. Use mayúsculas adecuadamente según las normas del español. Máximo 250 caracteres.")
    slug = models.SlugField(unique=True, help_text="Deber ser único.")
    description = models.TextField(help_text="Descripción de la categoría.")
    
    class Admin:
        pass
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['title']
        
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return "weblog/categories/%s/" % self.slug
        #return reverse('coltrane_category_detail', (), kwargs = {'slug': self.slug})

class Entry(models.Model):
    #Constants for the status field.
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'),
        (DRAFT_STATUS, 'Draft'),
        (HIDDEN_STATUS, 'Hidden'),
    )
    #Core Fields
    title = models.CharField(max_length=250, help_text="Título de máximo 250 caracteres.")
    excerpt = RichTextField(blank=True, help_text="Resumen")
    body = RichTextField(help_text="Texto de la entrada.")
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    #MetaData
    slug = models.SlugField(unique_for_date='pub_date', help_text="Only allows letters, numbers, underscores or hyphens.")
    author = models.ForeignKey(User)
    enable_comments = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS_CHOICES, default = LIVE_STATUS)
    #Categorization and tagging
    categories = models.ManyToManyField(Category)
    tags = TaggableManager(blank=True)
    
    class Meta:
        verbose_name_plural = 'Entries'
        ordering = ['-pub_date']
        
    class Admin:
        pass
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        #return "weblog/%s/%s/" % (self.pub_date.strftime("%Y/%m/%d").lower(), self.slug)
        return reverse('coltrane_entry_detail', kwargs = {'year': self.pub_date.strftime("%Y"), 'month':self.pub_date.strftime("%m"), 'day':self.pub_date.strftime("%d"),'slug':self.slug})
    
    