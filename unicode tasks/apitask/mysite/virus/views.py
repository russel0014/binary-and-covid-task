from django.shortcuts import render
from django.http import HttpResponse
import requests

from .forms import NameForm
from .models import COUNTRY
from django.db.models import Count


def get_name(request):
    #processing the form data by checking the method if post
    if request.method == 'POST':
       
        form = NameForm(request.POST)
    # for GET method  we'll create a blank form   
    else:
        form = NameForm()

    return render(request, 'index.html', {'form': form})

def yourname(request):
    if request.method == 'POST':    #getting the values by post request
            o1=request.POST.get('Name')
    if request.method == 'POST':
            o2=request.POST.get('email')
    if request.method == 'POST':
            q=request.POST.get('api')  #getting the country name

    
#api ka url
    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country":q}  #passing the country name
    
    headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "a67fd8a650msh4ac89d6ce0cc29fp1d63a6jsnde9d1edb5282"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    jsonResponse = response.json()#converting to json
    a={}#creating an empty dictionary in  which informaton would be passed
    
    #accesing the database
    cname1=COUNTRY(cname=q,name=o1,email=o2)
    cname1.save() #updating the database model COUNTRY
    rus= COUNTRY.objects.annotate(Count('cname'))#rus here is the queryset having the virus  information which is stored in database
    
    #if country name not found
    if jsonResponse['response']==[]:
        return HttpResponse('<h1> (づ-̩̩̩-̩̩̩_-̩̩̩-̩̩̩)づ srry we werent able to find your country kindly check if it was spelled right </h1>' )
    else:
        for x in jsonResponse["response"]:#if found
            a.update(x)#updating the dictionary 
            data=a
        params={'data':data,'o1':o1,'rus':rus}#passing parameters
        return render(request, 'yourname.html',params)
