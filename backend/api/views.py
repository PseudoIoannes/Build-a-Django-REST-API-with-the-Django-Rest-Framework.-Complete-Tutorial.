from django.http import JsonResponse
import json

from products.models import Product

def api_home(request):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data["title"] = model_data.title
        data["content"] = model_data.content
    return JsonResponse(data)
# Create your views here.

