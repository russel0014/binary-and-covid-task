from django.shortcuts import render
from django.http import HttpResponse
import requests

from .forms import NameForm
from .models import COUNTRY
from django.db.models import Count


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
        

    # if a GET (or any other method) we'll create a blank form

    else:
        form = NameForm()

    return render(request, 'index.html', {'form': form})

def yourname(request):
    if request.method == 'POST':
            o1=request.POST.get('Name')
    if request.method == 'POST':
            o2=request.POST.get('email')
    if request.method == 'POST':
            q=request.POST.get('api')

    

    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country":q}
    
    headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "a67fd8a650msh4ac89d6ce0cc29fp1d63a6jsnde9d1edb5282"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    jsonResponse = response.json()
    a={}
    cname1=COUNTRY(cname=q,name=o1,email=o2)
    cname1.save()
    rus= COUNTRY.objects.annotate(Count('cname'))
    
    for x in jsonResponse["response"]:
        a.update(x)
        print(a)
        data=a
    params={'data':data,'o1':o1,'rus':rus}
    return render(request, 'yourname.html',params)
