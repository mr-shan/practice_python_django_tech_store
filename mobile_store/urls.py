from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("mobiles/add-new/", views.AddMobileView.as_view()),
    path("<slug:slug>", views.mobile_details, name="mobile_details"),
]
