from operator import mod
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.views import View

from .models import Mobile

# Create your views here.


def index(request):
    all_mobiles = Mobile.objects.all().order_by('make')
    return render(request, "mobile_store/index.html", {
        "mobiles": all_mobiles
    })


def mobile_details(request, slug):
    # try:
    #     mobile = Mobile.objects.get(slug=slug)
    #     return render(request, "mobile_store/mobile_details.html", {
    #         "name": mobile.name,
    #         "make": mobile.make,
    #         "price": mobile.price,
    #         "rating": mobile.rating,
    #         "is_recommended": mobile.is_recommended
    #     })
    # except:
    #     raise Http404
    mobile = get_object_or_404(Mobile, slug=slug)
    return render(request, "mobile_store/mobile_details.html", {
        "name": mobile.name,
        "make": mobile.make.name,
        "price": mobile.price,
        "rating": mobile.rating,
        "is_recommended": mobile.is_recommended
    })


def store_file(file):
    with open("temp/image.png", mode="wb+") as nFile:
        for chunk in file.chunks():
            nFile.write(chunk)


class AddMobileView(View):
    def get(self, request):
        return render(request, "mobile_store/add_mobile.html")

    def post(self, request):
        store_file(request.FILES['image'])
        return HttpResponseRedirect("/mobiles/add-new/")
