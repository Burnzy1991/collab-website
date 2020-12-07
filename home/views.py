from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import HomeTest
# Create your views here.

def testimonial(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = HomeTest(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/aboutme')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = HomeTest()

    return render(request, 'home.html', {'form': form})
