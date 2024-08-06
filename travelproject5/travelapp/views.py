from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#def demo(request):
 #   return HttpResponse("hello world")
def demo(request):
    return render(request,"index.html")
#def about(request):
   # return render(request,'about.html')
#def contact(request):
   # return HttpResponse("hello world")
# def addition(request):
   # x=int(request.GET['num1'])
   # y=int(request.GET['num2'])
   # res=x+y
   # return render(request,"result.html",{'result':res})'''
