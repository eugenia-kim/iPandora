from rest_framework import routers
from django.conf.urls import include, url
from app.api.views import begin_proof, InputViewSet

router = routers.DefaultRouter()
router.register(r'input', InputViewSet)

urlpatterns = [
    url(r'^begin_proof/$', begin_proof),
    url(r'^', include(router.urls)),
]
