from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    picture = models.ImageField(upload_to='products/')
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Listed_vet(models.Model):
    name = models.CharField(max_length=30)
    adress = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name