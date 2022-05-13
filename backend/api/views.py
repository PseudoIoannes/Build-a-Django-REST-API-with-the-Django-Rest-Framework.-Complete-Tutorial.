from django.http import JsonResponse
import json

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer

@api_view(["GET"])
def api_home(request):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data["title"] = model_data.title
        # data["content"] = model_data.content
        data = ProductSerializer(instance).data
    return Response(data)
# Create your views here.


