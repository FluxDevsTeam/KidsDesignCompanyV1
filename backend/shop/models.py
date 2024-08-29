from django.db import models


class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField()
    stock = models.PositiveIntegerField(default=0)  # Quantity in stock
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def total_price(self):
        return self.stock * self.selling_price

    @property
    def profit(self):
        return self.selling_price - self.cost_price

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
