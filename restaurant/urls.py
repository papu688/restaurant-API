
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipes.views import ChefViewSet, RecipeViewSet, LoginViewSet

router = DefaultRouter()
router.register(r'chefs', ChefViewSet)
router.register(r'recipes', RecipeViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('login/', LoginViewSet.as_view())
]
