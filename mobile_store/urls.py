from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("<int:id>", views.mobile_details, name="mobile_details")
]
