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
    
    ordering = ['nom']
    
    ##----- AFFICHAGE DE L'IMAGE LORS DE LA MODOFICATION -------##
    readonly_fileds =['detail_Image']
    
    ##---- Les actions --------##
    actions = ('active', 'desactive')
    
    ##-------- FONCTION POUR ACTIVER LE STATUS --------##
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La sélection a été activé avec succès')
    active.short_descriprion = 'Activer les catégories sélectionnés'
    
    ##-------- FONCTION POUR DESACTIVER LE STATUS --------##
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La sélection a été désactivé avec succès')
    desactive.short_descriprion = 'Désactiver les catégories sélectionnés'
    
    def view_Image(self, obj):
        return mark_safe('<img src="{img_url}" width="100px" height="100px" />'.format(img_url=obj.image.url))
    
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
        
    ##------ Affichage des données par mois sélon le jour -----##
    date_hierarchy = ('date_add')
    
    ##------- Les champs cliquables --------##
    list_display_links = ('Image', 'nom',)
        
    ##------ PAGINATION DES DONNÉES ------##
    list_per_page = 3
        
    ordering = ['nom']
        
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
