from django.urls import path

from feedback.form import ReviewForm

from . import views

urlpatterns = [
    path("post-review", views.ReviewView.as_view()),
    path("success", views.SuccessView.as_view(), name="success"),
    path("review-list", views.ReviewListView.as_view()),
    path("review-list/<int:pk>", views.ReviewDetailsView.as_view())
]
