import random

from django.http import JsonResponse

def test_view(req):
    return JsonResponse({'alive': 'healthy'})

def random_number(req):
    rand_number = random.randint(0, 1000)
    print("Random number is %s" % (rand_number, ))
    return JsonResponse({'rand': rand_number})
