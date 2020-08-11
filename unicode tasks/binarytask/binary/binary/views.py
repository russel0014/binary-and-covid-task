from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request, 'index.html') 

#after submiting the range in index html we would get the anaylze template     
def analyze(request):
        #get the numbers 
        if request.method == 'POST':
            m1=request.POST.get('n1')
        if request.method == 'POST':
            m2=request.POST.get('n2')
        n1=int(m1)
        n2=int(m2)
        #make an empty list and then later append anaylising each decimal numbers
        p={}
        t={}
        for number in range(n1,n2+1):

            x=bin(number)  #converting decimal to binary
    
            p[number]=x     #appending the dictionary of converting decimal to binary
            new="11"
            if new in x:
                t[number]="true"   #appending the dictionary of true or false of consecutives 1's
            else :
                t[number]="false"
  

        
        
        params = {'ss':p,'ll':t}  #passing the parameters 
        return render(request, 'analyze.html', params) 