from django.db import models
from django.utils import timezone


class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    choices_body_type = (
        ('Break', 'Break'),
        ('Cabrio', 'Cabrio'),
        ('Coupe', 'Coupe'),
        ('Hatchback', 'Hatchback'),
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV')
    )
    body_type = models.CharField(max_length=20, choices=choices_body_type)
    make = models.CharField(max_length=20)
    car_model = models.CharField(max_length=20)
    choices_engine = (
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
    )
    engine = models.CharField(max_length=20, choices=choices_engine)
    horsepower = models.IntegerField()
    cylinder_capacity = models.FloatField(null=True, blank=True)
    choices_gearbox = (
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual'),
    )
    gearbox = models.CharField(max_length=20, choices=choices_gearbox)
    choices_transmission = (
        ('4x4', '4x4'),
        ('Rear', 'Rear'),
        ('Front', 'Front'),
    )
    transmission = models.CharField(
        max_length=20, choices=choices_transmission)

    choices_color = (
        ('Black', 'Black'),
        ('Brown', 'Brown'),
        ('Blue', 'Blue'),
        ('Green', 'Green'),
        ('Grey', 'Grey'),
        ('Red', 'Red'),
        ('White', 'White'),
        ('Yellow', 'Yellow'),
        ('Other Color', 'Other Color')
    )
    color = models.CharField(max_length=20, choices=choices_color)
    fabrication_year = models.IntegerField()
    kilometers = models.IntegerField()
    price = models.IntegerField()
    location = models.CharField(max_length=30)
    date_posted = models.DateField(default=timezone.now)
    picture1 = models.ImageField(
        blank=True, null=True, upload_to="pictures/%Y/%m/%d/")

    def __str__(self):
        return self.title


# Create your models here.