from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'place', views.PlaceViewSet, basename='place')
router.register(r'preset', views.PresetViewSet, basename='preset')
router.register(r'review', views.PresetViewSet, basename='review')
# router.register(r'image', views.PlaceImageViewSet, basename='image')
# router.register(r'placeDesc', views.PlaceDescViewSet, basename='placeDesc')
