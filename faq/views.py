from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def faq(request):
    context = {"a": "1", "b": "2"}
    return render(request, 'faq.html', context)
