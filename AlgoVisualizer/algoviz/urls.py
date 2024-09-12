from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:algo_id>/", views.array_viz, name="array_viz"),
]
