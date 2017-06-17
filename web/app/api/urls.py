from rest_framework import routers
from django.conf.urls import include, url

from app.api.views.BoxViewSet import BoxViewSet
from app.api.views.ForAllBoxViewSet import ForAllBoxViewSet
from app.api.views.StepViewSet import StepViewSet
from app.api.views.ToShowViewSet import ToShowViewSet
from app.api.views.GivenViewSet import GivenViewSet
from app.api.views.TypeViewSet import TypeViewSet
from app.api.views.begin_proof import begin_proof

router = routers.DefaultRouter()
router.register(r'given', GivenViewSet)
router.register(r'type', TypeViewSet)
router.register(r'toShow', ToShowViewSet)
router.register(r'step', StepViewSet)
router.register(r'box', BoxViewSet)
router.register(r'forallBox', ForAllBoxViewSet)

urlpatterns = [
    url(r'^begin_proof/$', begin_proof),
    url(r'^', include(router.urls)),
]
