from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.CharField(max_length=255)
    description = models.TextField()
    dosage = models.CharField(max_length=50)
    quantity_options = models.JSONField() # Store quantities as a list
    mrp = models.DecimalField(max_digits=10, decimal_places=2)
    concerns = models.JSONField()  # Store concerns as a list
    key_benefits = models.JSONField()  # Store key benefits as a list
    how_to_use = models.JSONField()  # Store usage instructions as a list
    precautions = models.JSONField()  # Store precautions as a list
    faqs = models.JSONField()  # Store FAQs as a list of dicts
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    reviewer_name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    review = models.TextField()

    def __str__(self):
        return self.reviewer_name

class DoctorsInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=100)
    depart_options=(
        ('sexologist','sexologist'),
    )
    department=models.CharField(max_length=100,choices=depart_options)
    image=models.ImageField(upload_to='doctor_image')
    qualification=models.CharField(max_length=150)
    experience=models.IntegerField()
    phone=PhoneNumberField()
    email=models.EmailField(max_length=254)
    
    def __str__(self):
        return self.name



class SliderImagesHome(models.Model):
    image1=models.ImageField(upload_to='slider_home_img_1')
    
        

