from django.db import models

class carsList(models.Model):
    carimage=models.ImageField(upload_to='media/store/images/thumbimages',default="",blank=True)
    carname=models.CharField(max_length=20)
    carrent=models.IntegerField()
    carpdf=models.FileField(upload_to='media/store/pdfs',default="",blank=True)
    def __str__(self):
        return self.carname


# Create your models here.
