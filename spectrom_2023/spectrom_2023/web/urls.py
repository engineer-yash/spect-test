from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),

    path("",views.showslides),

    path('<int:event_name>/' , views.Events , name = "event"),

    path('Events/<event_name>/' , views.Events , name = "event"),
]
