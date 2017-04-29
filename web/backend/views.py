from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET'])
def init_dec(req):
    return JsonResponse({'dec': True})