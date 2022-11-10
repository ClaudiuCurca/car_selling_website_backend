from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()


class Listing(models.Model):
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
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
    mileage = models.IntegerField()
    price = models.IntegerField()
    location = models.CharField(max_length=30)
    date_posted = models.DateTimeField(default=timezone.now)
    picture1 = models.ImageField(
        blank=True, null=True, upload_to="pictures/%Y/%m/%d/")
    picture2 = models.ImageField(
        blank=True, null=True, upload_to="pictures/%Y/%m/%d/")
    picture3 = models.ImageField(
        blank=True, null=True, upload_to="pictures/%Y/%m/%d/")
    picture4 = models.ImageField(
        blank=True, null=True, upload_to="pictures/%Y/%m/%d/")
    picture5 = models.ImageField(
        blank=True, null=True, upload_to="pictures/%Y/%m/%d/")
    seller_name = models.CharField(max_length=30)
    seller_phone_number = models.CharField(max_length=30)

    def __str__(self):
        return self.title


# Create your models here.
