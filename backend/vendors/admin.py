from django.contrib import admin

# Register your models here.
from .models import Vendor, District, Subdistrict

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'shop_name', 'phone_number', 'is_approved', 'created_at', 'district', 'subdistrict', 'address_1']
    list_filter = ['is_approved']
    search_fields = ['first_name', 'last_name', 'shop_name', 'email']
    list_editable = ['is_approved']

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Subdistrict)
class SubdistrictAdmin(admin.ModelAdmin):
    list_display = ['name', 'district']
    search_fields = ['name']
    list_filter = ['district']