from rest_framework import serializers
from .models import District, Subdistrict, Vendor

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'name']

class SubdistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subdistrict
        fields = ['id', 'name', 'district']

class VendorSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = [
            'first_name',
            'last_name',
            'shop_name',
            'address_1',
            'address_2',
            'subdistrict',
            'district',
            'email',
            'phone_number',
            'password',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
        }
    def create (self, validate_data):
        vendor = Vendor.objects.create(**validate_data)
        return vendor
