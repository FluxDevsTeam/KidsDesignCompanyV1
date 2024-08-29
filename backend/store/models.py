from django.db import models


class RawMaterial(models.Model):

    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=20)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def cost_per_unit(self):
        return self.price / self.quantity

    category = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="raw_materials/", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]



