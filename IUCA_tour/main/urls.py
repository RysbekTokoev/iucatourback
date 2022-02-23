from django.urls import include, path
from .routers import *
from .views import get_image_view

app_name = 'main'
urlpatterns = [
    path('', include(router.urls)),
    path('get_map/', get_image_view),
]
