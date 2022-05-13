from django.http import JsonResponse
import json

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request):
    # instance = Product.objects.all().order_by("?").first()
    # data = request.data
    # if instance:
    #     data = ProductSerializer(instance).data
    data = request.data
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
# Create your views here.


