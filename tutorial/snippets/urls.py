from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views


# create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'snippets', views.UserViewSet)


# the API urls are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]
