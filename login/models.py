from django.db import models
class Foto(models.Model):
    id=models.BigAutoField(primary_key=True)
    foto=models.ImageField(upload_to='https://drive.google.com/drive/folders/1LPpRutERanX66GTEiFCHiFWc7TmnqELl?usp=sharing')
    #foto=models.ImageField(upload_to='static/imagenes/')
