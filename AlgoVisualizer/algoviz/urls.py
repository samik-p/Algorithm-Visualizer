from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("array/", views.array, name="array"),
    path("array/binary_search/", views.array_binary_search, name="array_binary_search"),
]
