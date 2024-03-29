from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import RecipeViewSet


router = DefaultRouter()
router.register('', RecipeViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]