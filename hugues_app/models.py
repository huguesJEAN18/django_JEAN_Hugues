from django.db import models
from django.contrib.auth.models import User

class Planification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_planification = models.DateTimeField()
    lieu = models.CharField(max_length=100)


class Suivi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_suivi = models.DateTimeField()
    action = models.CharField(max_length=100)
   
class Vol(models.Model):
    compagnie = models.CharField(max_length=100)
    numero_vol = models.CharField(max_length=50)
    depart = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date_depart = models.DateTimeField()
    date_arrivee = models.DateTimeField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    
class Reservation(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    vol = models.ForeignKey(Vol, on_delete=models.CASCADE)
    date_reservation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.utilisateur} - {self.vol}"