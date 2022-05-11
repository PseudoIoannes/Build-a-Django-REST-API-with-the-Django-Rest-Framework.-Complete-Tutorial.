from django.http import JsonResponse

def api_home(request):
    return JsonResponse({"message": "Django api response!"})
# Create your views here.

