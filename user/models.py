from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField("Имя", max_length=100)
    frist_name = models.CharField( "Фамиля", max_length=55)
    age = models.BigIntegerField("Дата рождения")
    description = models.TextField("О себе")

    def __str__(self):
        return self.name