from django.urls import include, path
from vendors import views
app_name = 'vendors'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
]

