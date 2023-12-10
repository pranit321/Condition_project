from django.shortcuts import render

# Create your views here.

def condition(request):
    d={'a':10000,'b':2000,'c':3000}
    return render(request,'condition.html',d)