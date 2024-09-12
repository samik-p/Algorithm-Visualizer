from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    response = """
    <p>This is the algoviz index.</p>
    <ol>
        <li><a href = "array/">Array</a></li>
        <li><a href = "tree/">Tree</a></li>
        <li><a href = "graph/">Graph</a></li>
    </ol>
    """

    return HttpResponse(response)


def array(request):
    response = """
    <p>This is the landing page for array data structure.</p>
    
    <p>Search Algos</p>
    <ol>
        <li><a href = "binary_search/">Binary Search</a></li>
    </ol>
    <p>Sort Algos</p>
    <ol>
        <li><a href = "bubble_sort/">Bubble Sort</a></li>
        <li><a href = "merge_sort/">Merge Sort</a></li>
        <li><a href = "insert_sort/">Insert Sort</a></li>
        <li><a href = "bucket_sort/">Bucket Sort</a> </li>
    </ol>
    """
    return HttpResponse(response)

def tree(request):
    response = """
    <p>This is the landing page for tree data structure.</p>
   
    """
    return HttpResponse(response)

def graph(request):
    response = """
    <p>This is the landing page for graph data structure.</p>
   
    """
    return HttpResponse(response)


def array_binary_search(request):
    response = "This is the page for binary search for arrays."
    return HttpResponse(response)


def array_bubble_sort(request):
    response = f"This is the page for bubble sort for arrays"
    return HttpResponse(response)


def array_merge_sort(request):
    response = f"This is the page for merge sort for arrays"
    return HttpResponse(response)


def array_insert_sort(request):
    response = f"This is the page for insert sort for arrays"
    return HttpResponse(response)


def array_bucket_sort(request):
    response = f"This is the page for bucket sort for arrays"
    return HttpResponse(response)
