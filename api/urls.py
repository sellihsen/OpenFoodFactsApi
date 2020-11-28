from django.urls import path

from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include auth & login URLs for the browsable API.
urlpatterns = [
    # Get Product Url
    path('api/product/<int:GTIN>/', views.get_product),
]
