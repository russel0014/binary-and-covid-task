from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
def analyze(request):
        #get the numbers
        if request.method == 'POST':
            m1=request.POST.get('n1')
        if request.method == 'POST':
            m2=request.POST.get('n2')
        n1=int(m1)
        n2=int(m2)
        p={}
        t={}
        for number in range(n1,n2+1):

            x=bin(number)
    
            p[number]=x
            new="11"
            if new in x:
                t[number]="true"
            else :
                t[number]="false"
  

        
        
        params = {'ss':p,'ll':t}
        return render(request, 'analyze.html', params)