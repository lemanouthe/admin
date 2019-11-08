from django.contrib import admin
##-------- IMPORTATION DES MODELS DE L'APPLICATION ---------##
from . import models
##--------- IMPORTATION DE MARK SAFE POUR L'AFFICHAGE D'UNE IMAGE SUR LA PARTIE ADMIN --------##
from django.utils.safestring import mark_safe
# Register your models here.

## register inline ##

class SousCategorieInline(admin.TabularInline):
    model = models.SousCategrorie
    extra = 0
    
class ProduitInline(admin.TabularInline):
    model = models.Produit
    extra = 0

##------- CREATION D'UN MODELE ---------##
@admin.register(models.Categorie)

##--------- CREATION DE LA CLASSE ------##
class CategorieAdmin(admin.ModelAdmin):
    ##------ les champs et les rélations -----##
    list_display = (
        'view_Image',    
        'nom',
        'date_add',
        'date_upd',
        'status',
    )
    ##---- Filtrer les données -----##
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )
    ##---- Champs de recherche ----##
    search_fields = (
        'nom',
    )
    
    inlines = [SousCategorieInline]
    
    ##------ Affichage des données par mois sélon le jour -----##
    date_hierarchy = ('date_add')
    
    ##------- Les champs cliquables --------##
    list_display_links = ('view_Image', 'nom',)
    
    ##------ PAGINATION DES DONNÉES ------##
    list_per_page = 3
    
    ##------- Ordonne les données par nom ------## 
    ordering = ['nom']
    
    ##----- AFFICHAGE DE L'IMAGE LORS DE LA MODOFICATION -------##
    readonly_fields =['detail_Image']
    
    ##---- Les actions --------##
    actions = ('active', 'desactive')
    
    ##-------- FONCTION POUR ACTIVER LE STATUS --------##
    def active(self, request, queryset):
        ##------ PERMET DE RENDRE LE STATUS A TRUE ------------##
        queryset.update(status=True)
        ##------- AFFICHE LE MESSAGE -----------##
        self.message_user(request, 'La sélection a été activé avec succès')
    ##--------- LE NOM DANS ACTIONS ------------##
    active.short_descriprion = 'Activer les catégories sélectionnés'
    
    ##-------- FONCTION POUR DESACTIVER LE STATUS --------##
    def desactive(self, request, queryset):
         ##------ PERMET DE RENDRE LE STATUS A FALSE ------------##
        queryset.update(status=False)
         ##------- AFFICHE LE MESSAGE -----------##
        self.message_user(request, 'La sélection a été désactivé avec succès')
     ##--------- LE NOM DANS ACTIONS ------------##
    desactive.short_descriprion = 'Désactiver les catégories sélectionnés'
     
    ##------- FONCTION POUR L'AFFICHACHE DE L'IMAGE SUR L'ADMIN -----------##
    def view_Image(self, obj):
        return mark_safe('<img src="{img_url}" width="100px" height="100px" />'.format(img_url=obj.image.url))
    
    ##------- FONCTION POUR L'AFFICHACHE DE L'IMAGE SUR L'ADMIN -----------##
    def detail_Image(self, obj):
        return mark_safe('<img src="{img_url}" width="100px" height="100px" />'.format(img_url=obj.image.url))

@admin.register(models.SousCategrorie)
class SousCategorieAdmin(admin.ModelAdmin):
##------ les champs et les rélations -----##
    list_display = (
        'categorie_id',
        'nom',
        'date_add',
        'date_upd',
        'status',
        'Image',
    )
    ##---- Filtrer les données et les rélations -----##
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'categorie_id',
    )
    ##---- Champs de recherche ----##
    search_fields = (
        'categorie_id',
        'nom',
    )
    
    inlines = [ProduitInline]

        
    ##------ Affichage des données par mois sélon le jour -----##
    date_hierarchy = ('date_add')
    
    ##------- Les champs cliquables --------##
    list_display_links = ('Image', 'nom',)
        
    ##------ PAGINATION DES DONNÉES ------##
    list_per_page = 3
        
    ordering = ['nom']
    
    readonly_fields =['detImage']

    ##---- Les actions --------##
    actions = ('active', 'desactive')
        
    ##-------- FONCTION POUR ACTIVER LE STATUS --------##
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La sélection a été activé avec succès')
    active.short_descriprion = 'Activer les souscatégories sélectionnés'
        
    ##-------- FONCTION POUR DESACTIVER LE STATUS --------##
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La sélection a été désactivé avec succès')
    desactive.short_descriprion = 'Désactiver les souscatégories sélectionnés'
        
    def Image(self, obj):
        return mark_safe('<img src="{url}" width="100px" height="100px" />'.format(url=obj.image.url))
    
    def detImage(self, obj):
        return mark_safe('<img src="{url}" width="100px" height="100px" />'.format(url=obj.image.url))

@admin.register(models.Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = (
        'souscategorie',
        'titre',
        'date_add',
        'date_upd',
        'status',
        'produit_Image',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'souscategorie',
    )
    ##---- Champs de recherche ----##
    search_fields = (
        'souscategorie',
        'tague',
        'nom',
    )
    fieldsets = [
        ('Titre et Visibilité', {'fields': ['titre', 'status']}),
        ('Description et Image', {'fields': ['description', 'image']}),
        ('Tague et Souscategorie', {'fields': ['tague', 'souscategorie']}),
    ]
    
    filter_horizontal = ('tague',)
    
    actions = ('active', 'desactive')
    
    list_per_page = 3
        
    ordering = ['titre']
    
    list_display_links = ('produit_Image', 'titre',)
    
    date_hierarchy = ('date_add')
    
    readonly_fields =['proImage']


        
    ##-------- FONCTION POUR ACTIVER LE STATUS --------##
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La sélection a été activé avec succès')
    active.short_descriprion = 'Activer les produits sélectionnés'
        
    ##-------- FONCTION POUR DESACTIVER LE STATUS --------##
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La sélection a été désactivé avec succès')
    desactive.short_descriprion = 'Désactiver les produits sélectionnés'
    
    def produit_Image(self, obj):
        return mark_safe('<img src="{url}" width="100px" height="100px" />'.format(url=obj.image.url))
    
    def proImage(self, obj):
        return mark_safe('<img src="{url}" width="100px" height="100px" />'.format(url=obj.image.url))
    
@admin.register(models.Tague)
class TagueAdmin(admin.ModelAdmin):
    list_display = (
        'nom',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )
    search_fields = (
        'nom',
    )
    actions = ('active', 'desactive')
    list_per_page = 3
            
    ordering = ['nom']
        
    list_display_links = ('nom',)
        
    date_hierarchy = ('date_add')
    
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La sélection a été activé avec succès')
    active.short_descriprion = 'Activer les tagues sélectionnés'
            
    ##-------- FONCTION POUR DESACTIVER LE STATUS --------##
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La sélection a été désactivé avec succès')
    desactive.short_descriprion = 'Désactiver les tagues sélectionnés'
