from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    response = """
    <p>This is the algoviz index.</p>
    <ol>
        <li><a href="array/">Array</a></li>
    </ol>
    """

    return HttpResponse(response)


def array(request):
    return HttpResponse("This is the landing page for array data structure")


def array_binary_search(request):
    response = f"This is the page for binary search for arrays."
    return HttpResponse(response)
