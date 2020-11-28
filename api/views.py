from openfoodfacts import products
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create Http Get to return a json file loaded from openfoodfacts when executing products.get_product methode with parameter GTIN
@api_view(['GET'])
def get_product(request, GTIN):
    return Response(products.get_product(str(GTIN)))
