from django.contrib.auth import get_user_model
from django.db import models

class Utilisateur(models.Model):
    CITOYEN = "citizen"
    AUTORITE = "autority"
    ENTREPRISE = "supplier"
    
    ROLE_CHOICES = [
        (CITOYEN, "Citoyen"),
        (AUTORITE, "Autorite"),
        (ENTREPRISE, "Entreprise"),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=CITOYEN)
    address = models.CharField(max_length=20, blank=True, default='open@gmail.com')  
    password=models.CharField(max_length=10, blank=True, default='open@gmail.com')
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    date_joined=models.BooleanField(default=False)
    is_verified=models.BooleanField(default=False)
    
    def est_citoyen(self):
        return self.role == self.CITOYEN

    def est_autorite(self):
        return self.role == self.AUTORITE

    def est_entreprise(self):
        return self.role == self.ENTREPRISE


# Récupère le modèle personnalisé d'utilisateur
Utilisateur = get_user_model()

class Citoyen(Utilisateur):
    first_name= models.CharField(max_length=100, blank=True, null=True) 
    last_name=  models.CharField(max_length=100, blank=True, null=True) 
    profession = models.CharField(max_length=100, blank=True, null=True)  
    birth_date = models.DateField(blank=True, null=True)  
    enabled_notifications =models.BooleanField(defaut='True')
    class Meta:
        verbose_name = "Citoyen"
        verbose_name_plural = "Citoyens"

class Autority(models.Model):
    name_organization = models.CharField(max_length=100, blank=True, null=True)  
    class Meta:
        verbose_name = "autorite"
        verbose_name_plural = "autorites"

class Supplier(Utilisateur):
    nom_entreprise = models.CharField(max_length=100, blank=True, null=True) 
    secteur_activite= models.CharField(max_length=100, blank=True, null=True) 
    class Meta:
        verbose_name = "entreprise"
        verbose_name_plural = "entreprises"