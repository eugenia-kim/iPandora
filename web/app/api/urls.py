from rest_framework import routers
from django.conf.urls import include, url

from app.api.views.ToShowViewSet import ToShowViewSet
from app.api.views.GivenViewSet import GivenViewSet
from app.api.views.TypeViewSet import TypeViewSet
from app.api.views.begin_proof import begin_proof

router = routers.DefaultRouter()
router.register(r'given', GivenViewSet)
router.register(r'type', TypeViewSet)
router.register(r'toShow', ToShowViewSet)

urlpatterns = [
    url(r'^begin_proof/$', begin_proof),
    url(r'^', include(router.urls)),
]
