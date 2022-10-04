

from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register('todoApp', views.TodoViewset)
urlpatterns = [
    path('', include(router.urls)),
]
