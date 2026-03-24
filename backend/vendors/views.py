from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import District, Subdistrict
from .serializers import VendorSignupSerializer, DistrictSerializer, SubdistrictSerializer

# Create your views here.
def signup(request):
    return render(request, 'vendors/signup.html')

class VendorSignupView(APIView):
    def post(self, request):
        serializer = VendorSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'Vendor registered successfully'},
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class DistrictListView(APIView):
    def get(self, request):
        search = request.query_params.get('search', '')
        districts = District.objects.filter(name__icontains=search)
        serializer = DistrictSerializer(districts, many=True)
        return Response(serializer.data)

class SubdistrictListView(APIView):
    def get(self, request, district_id):
        subdistricts = Subdistrict.objects.filter(district_id=district_id)
        serializer = SubdistrictSerializer(subdistricts, many=True)
        return Response(serializer.data)