from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from . import views

routers = routers.DefaultRouter()
routers.register('role', views.RoleViewSet)
routers.register('user', views.UserViewSet)
routers.register('location', views.LocationViewSet)
routers.register('room', views.RoomViewSet)
routers.register('board', views.BoardViewSet)
routers.register('data', views.DataViewSet)
routers.register('report', views.ReportViewSet)

urlpatterns = [
    url('^', include(routers.urls)),
]



