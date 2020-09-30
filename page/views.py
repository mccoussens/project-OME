from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import LocationForm
import time
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = LocationForm(request.POST or None)
        if form.is_valid():
            name1 = form.cleaned_data['your_name']
            lat1 = form.cleaned_data['your_latitude']
            lon1 = form.cleaned_data['your_longitude']
            name2 = form.cleaned_data['their_name']
            lat2 = form.cleaned_data['their_latitude']
            lon2 = form.cleaned_data['their_longitude']

            # Do the processing and api calls here
            # Save an image in the media folder and the /location 
            # url will just display the image
            api_response = "3902942048082048"

            time.sleep(3)
            return HttpResponseRedirect('/location')

    # if a GET (or any other method) we'll create a blank form
    else:
        api_response = None
        form = LocationForm()

    context = {
        'form': form,
        'api_response': api_response
    }

    return render(request, 'index.html', context)

def location(request):
    return render(request, 'location.html')