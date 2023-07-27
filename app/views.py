from django.shortcuts import render, redirect
from .models import Phone


def index_view(request):
    return redirect("catalog")


def catalog_view(request):
    sort_by = request.GET.get("sort", "name")
    if sort_by == "name":
        phones = Phone.objects.order_by("name")
    elif sort_by == "min_price":
        phones = Phone.objects.order_by("price")
    elif sort_by == "max_price":
        phones = Phone.objects.order_by("-price")
    else:
        phones = Phone.objects.all()
    return render(request, "catalog.html", {"phones": phones})


def phone_view(request, slug):
    phone = Phone.objects.get(slug=slug)
    return render(request, "phone.html", {"phone": phone})
