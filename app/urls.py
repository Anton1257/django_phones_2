from django.urls import path
from app.views import catalog_view, index_view, phone_view

urlpatterns = [
    path("", index_view),
    path("catalog/", catalog_view, name="catalog"),
    path("catalog/<slug:slug>/", phone_view, name="phone"),
]
