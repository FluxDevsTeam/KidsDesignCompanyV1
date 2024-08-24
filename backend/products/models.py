from django.db import models
import ast


class ListField(models.TextField):
    """
    Custom field to store a Python list as a comma-separated string.
    """
    def to_python(self, value):
        if not value:
            return []
        if isinstance(value, list):
            return value
        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value
        return ",".join(str(item) for item in value)


class Product(models.Model):
    name = models.CharField(max_length=100)
    raw_materials = models.TextField()
    quotation = models.DecimalField(max_digits=10, decimal_places=2)
    dimensions = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    design = models.TextField()
    artisan_id = models.PositiveIntegerField()
    artisan_cost = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)

    def total_production_cost(self):
        return self.cost_price + self.artisan_cost

    images = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Quotation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quotation = ListField()


class RawMaterialUsed(models.Model):
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=20)  # e.g., "kg," "meters," etc.
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="raw_materials/", blank=True, null=True)

    def total_price(self):
        return self.cost_per_unit / self.quantity

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
