
from .views import home, productDetail
from .import views
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('product/<int:id>/', productDetail, name='productDetail'),  # Ensure this line exists
]