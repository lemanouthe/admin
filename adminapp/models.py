from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField
from django.contrib.postgres.fields import IntegerRangeField
from django.contrib.postgres.fields import DateTimeRangeField
from django_countries.fields import CountryField

# Create your models here.

def default_thing():
    return ['M']

class Categorie(models.Model):
    nom = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='categorie/%Y/%m/%d/')
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.nom


class SousCategrorie(models.Model):
    nom = models.CharField(max_length=250)
    categorie_id = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='categorie')
    image = models.ImageField(upload_to='souscategorie/%Y/%m/%d/')
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nom

class Tague(models.Model):
    nom = models.CharField(max_length=250)
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom


class Produit(models.Model):
    souscategorie = models.ForeignKey(SousCategrorie, on_delete=models.CASCADE, related_name='produit_souscategorie')
    tague = models.ManyToManyField(Tague, related_name='produit_tag')
    titre = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='produit/%Y/%m/%d/')
    taille = ArrayField(models.CharField(max_length=10, blank=True, null=True), default=default_thing)
    family = JSONField()
    prix = IntegerRangeField()
    # periode = DateTimeRangeField(null=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titre


class Person(models.Model):
    name = models.CharField(max_length=100)
    country = CountryField(countries_flag_url='//flags.example.com/{code}.png')
    
class Incident(models.Model):
    title = models.CharField(max_length=100)
    countries = CountryField(multiple=True)
