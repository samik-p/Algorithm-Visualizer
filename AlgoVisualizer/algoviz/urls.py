from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("array/", views.array, name="array"),
    path("array/binary_search/", views.array_binary_search, name = "array_binary_search"),
    path("array/bubble_sort/", views.array_bubble_sort, name ="array_bubble_sort"),
    path("array/merge_sort/", views.array_merge_sort, name ="array_merge_sort"),
    path("array/insert_sort/", views.array_insert_sort, name ="array_insert_sort"),
    path("array/bucket_sort/", views.array_bucket_sort, name ="array_bucket_sort"),
]
