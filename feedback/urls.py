from django.urls import path

from . import views

urlpatterns = [
    path("post-review", views.ReviewView.as_view()),
    path("success", views.success)
]
