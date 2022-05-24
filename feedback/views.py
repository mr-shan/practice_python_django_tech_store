from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

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


def success(request):
    return render(request, "feedback/success.html")


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
