from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def contact(request):
    context = {"a": "1", "b": "2"}
    return render(request, 'contact.html', context)
