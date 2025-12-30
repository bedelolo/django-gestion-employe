from django.db import models

class Employe(models.Model):
    Nom=models.CharField(max_length=100)
    Prenom=models.CharField(max_length=100, null=True)
    Email=models.EmailField()
    Telephone=models.CharField(max_length=20, null=True)
    Poste=models.CharField(max_length=100)
    Salaire=models.DecimalField(max_digits=100 , decimal_places=2)
    Date_Embauche=models.DateField(null=True)

    def __str__(self):
        return f"{self.Nom} {self.Prenom}"
