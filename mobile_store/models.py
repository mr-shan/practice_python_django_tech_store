from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=5)

    def __str__(self) -> str:
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Mobile(models.Model):
    name = models.CharField(max_length=50)
    make = models.ForeignKey(Company, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True, validators=[
                                 MaxValueValidator(10), MinValueValidator(1)])
    is_recommended = models.BooleanField(default=False)
    image = models.URLField(
        default="https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Icons8_flat_cell_phone.svg/768px-Icons8_flat_cell_phone.svg.png")
    slug = models.SlugField(
        default="", null=False, db_index=True, unique=True, blank=True)
    released_countries = models.ManyToManyField(Country)

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.make} {self.name}")
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("mobile_details", kwargs={"slug": self.slug})

    def __str__(self) -> str:
        return f"{self.make.name} {self.name} @ {self.price}."
