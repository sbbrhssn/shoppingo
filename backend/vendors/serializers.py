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
    password = serializers.CharField(
        min_length=8,
        error_messages={'min_length': 'Password must be at least 8 characters.'}
    )
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
    def create (self, validated_data):
        vendor = Vendor.objects.create(**validated_data)
        return vendor
