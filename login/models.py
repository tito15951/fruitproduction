from django.db import models
class Foto(models.Model):
    id=models.BigAutoField(primary_key=True)
    foto=models.ImageField(upload_to='imagenes/')
