from django.db import models
from customers.models import Customer


class Project(models.Model):
    unique_id = models.CharField(max_length=20, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    products = models.ManyToManyField("Product", related_name="projects")
    status = models.CharField(max_length=50)

    start_date = models.DateField()
    deadline = models.DateField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    total_production_cost = models.DecimalField(max_digits=10, decimal_places=2)
    running_expenses = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Project for {self.customer} ({self.unique_id})"

    class Meta:
        ordering = ["deadline"]

