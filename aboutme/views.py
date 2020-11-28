from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def aboutme(request):
    context = {"a": "1", "b": "2"}
    return render(request, 'aboutme.html', context)
