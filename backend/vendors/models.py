from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

# Create your models here.

class District(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Subdistrict(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.district.name}"

class Vendor(models.Model):
    vendor_id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=500, unique=True)
    address_1 = models.CharField(max_length=500)
    address_2 = models.CharField(max_length=500, blank=True)
    subdistrict = models.ForeignKey(Subdistrict, on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11, unique=True, validators=[RegexValidator(r'^\d{11}$', "Enter 11 digit phone number")])
    password = models.CharField(max_length=15, validators=[MinLengthValidator(8, 'Password must be at least 8 characters long.')])
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.shop_name}"

