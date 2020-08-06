from django.urls import path     
from . import views

urlpatterns = [
    path('home', views.home),
    path('addTrip',views.addTrip),
    path('createTrip',views.createTrip),
    path('<id>/edit',views.editTrip),
    path('<id>/update',views.updateTrip),
    path('<id>/<userid>/join',views.joinTrip),
    path('<id>/<userid>/removeJoin',views.removeJoin),
    path('<id>/destroy',views.destroyTrip),
    path('<id>/tripDetails',views.tripDetails),


]