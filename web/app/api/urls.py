from django.conf.urls import url

from app.views import init_dec

urlpatterns = [
    url(r'^init_dec/?$', init_dec, name='initial declaration')
    ]

