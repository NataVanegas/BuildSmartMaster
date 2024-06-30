# apps/constructionMaterial/models.py
from django.db import models

class MaterialCategory(models.Model):
    """
    Modelo que representa una categoría de materiales de construcción.

    Atributos:
        name (CharField): Nombre de la categoría, con un máximo de 100 caracteres.
        description (TextField): Descripción opcional de la categoría.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        """
        Devuelve una representación en cadena del modelo.
        """
        return self.name

class Material(models.Model):
    """
    Modelo que representa un material de construcción.

    Atributos:
        name (CharField): Nombre del material, con un máximo de 100 caracteres.
        description (TextField): Descripción opcional del material.
        category (ForeignKey): Categoría a la que pertenece el material. Relación muchos a uno con MaterialCategory.
        unit_price (DecimalField): Precio unitario del material, con un máximo de 10 dígitos en total y 2 decimales.
        stock_quantity (PositiveIntegerField): Cantidad de material en stock.
        image (ImageField): Imagen opcional del material. Se guarda en la carpeta 'materials/'.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.ForeignKey(MaterialCategory, on_delete=models.CASCADE)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='materials/', blank=True, null=True)

    def __str__(self):
        return self.name
