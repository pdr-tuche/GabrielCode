from django.contrib import admin
from django.urls import path, include
from restaurante.views import FuncionarioViewSet, EnderecoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('funcionario', FuncionarioViewSet)
router.register('endereco', EnderecoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
