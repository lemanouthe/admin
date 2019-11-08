from django.db import models

# Create your models here.

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
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titre
