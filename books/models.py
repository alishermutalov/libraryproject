from django.db import models
from django.conf import settings
from django.utils.text import slugify
# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="First Name", null=True, blank=True)
    slug = models.SlugField(verbose_name="Slug")
    about_author = models.TextField(verbose_name="About", null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.first_name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.first_name
    
    
class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    slug = models.SlugField(verbose_name="Slug")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    publication_date = models.DateField(null=True, blank=True)
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character ISBN number',null=True, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2,null=True, blank=True)
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title
    