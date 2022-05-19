from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

# Create your models here.


class Mobile(models.Model):
    name = models.CharField(max_length=50)
    make = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(null=True, max_digits=4, decimal_places=2, validators=[
                                 MaxValueValidator(10), MinValueValidator(1)])
    is_recommended = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("mobile_details", kwargs={"id": self.id})

    def __str__(self) -> str:
        return f"{self.make} {self.name} @ {self.price}."
