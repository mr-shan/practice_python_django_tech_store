from django.shortcuts import render
from django.http import Http404

from .models import Mobile

# Create your views here.


def index(request):
    all_mobiles = Mobile.objects.all().order_by('make')
    return render(request, "mobile_store/index.html", {
        "mobiles": all_mobiles
    })


def mobile_details(request, id):
    try:
        mobile = Mobile.objects.get(pk=id)
        return render(request, "mobile_store/mobile_details.html", {
            "name": mobile.name,
            "make": mobile.make,
            "price": mobile.price,
            "rating": mobile.rating,
            "is_recommended": mobile.is_recommended
        })
    except:
        raise Http404
