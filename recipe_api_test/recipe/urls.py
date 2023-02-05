from django.urls import path
from .apis import RecipeList
from rest_framework import routers
from .apis import RecipeList


router = routers.DefaultRouter()
router.register(r'recipes', RecipeList)

urlpatterns = [
    path('recipes/', RecipeList.as_view(), name='recipes'),
]