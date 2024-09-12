from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("This is the algoviz index")


def array_viz(request, algo_id):
    response = f"You're looking at the array visualization for algo id {algo_id}"
    return HttpResponse(response)
