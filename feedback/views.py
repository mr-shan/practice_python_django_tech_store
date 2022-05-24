from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView

from .form import ReviewForm
from .models import ReviewModel

# Create your views here.


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return self.send_review_template(request, form)

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            self.save_review(form)
            return HttpResponseRedirect(redirect_to="success")

        return self.send_review_template(request, form)

    def send_review_template(self, request, form):
        return render(request, "feedback/add_review.html", {
            "form": form
        })

    def save_review(self, form):
        review = ReviewModel(
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            text=form.cleaned_data['review_text'],
            rating=form.cleaned_data['rating']
        )
        review.save()


class SuccessView(TemplateView):
    template_name = "feedback/success.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Your review is submitted successfully!"
        return context


class ReviewListView(TemplateView):
    template_name = "feedback/review_list.html"

    def get_context_data(self, **kwargs):
        reviews = ReviewModel.objects.all().order_by('-pk')
        context = super().get_context_data(**kwargs)
        context['reviews'] = reviews
        return context


class ReviewDetailsView(DetailView):
    template_name = "feedback/review-details.html"
    model: ReviewModel


# def success(request):
#     return render(request, "feedback/success.html")


# Creating method instead of class.
# def reviews(request):
#     if request.method == "POST":
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             review = ReviewModel(
#                 name=form.cleaned_data['name'],
#                 email=form.cleaned_data['email'],
#                 text=form.cleaned_data['review_text'],
#                 rating=form.cleaned_data['rating']
#             )
#             review.save()
#             return HttpResponseRedirect(redirect_to="success")
#         else:
#             return render(request, "feedback/add_review.html", {
#                 "form": form
#             })

#     return render(request, "feedback/add_review.html", {
#         "form": ReviewForm
#     })
