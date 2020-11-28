from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def services(request):
    context = {"a": "1", "b": "2"}
    return render(request, 'services.html', context)
