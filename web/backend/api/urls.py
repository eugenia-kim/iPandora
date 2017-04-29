from django.conf.urls import url

from backend.testviews import test_view, random_number
from backend.views import init_dec

urlpatterns = [
    url(r'^health/?$', test_view, name='health_check'),
    url(r'^rand/?$', random_number, name='random number'),
    url(r'^init_dec/?$', init_dec, name='initial declaration')
]