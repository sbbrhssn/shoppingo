from django.urls import include, path
from vendors import views
app_name = 'vendors'

urlpatterns = [
    path('', views.signup, name='signup'),
    path('signup/', views.VendorSignupView.as_view(), name='vendor_signup'),
    path('districts/', views.DistrictListView.as_view(), name='district_list'),
    path('districts/<int:district_id>/subdistricts/', views.SubdistrictListView.as_view(), name='subdistrict_list'),
]

