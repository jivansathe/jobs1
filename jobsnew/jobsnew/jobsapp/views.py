from django.shortcuts import render
from django.http import HttpResponse

def Mumbaijobs(request):
    s1= '<h1> Mumbai Jobs information...!!!<h1>'
    return HttpResponse(s1)

def Punejobs(request):
    s2= '<h1> Pune Jobs information...!!!<h1>'
    return HttpResponse(s2)

def Delhijobs(request):
    s3= '<h1> Delhi Jobs information...!!!<h1>'
    return HttpResponse(s3)

def Hyderabadjobs(request):
    s4= '<h1> Hyderabad Jobs information...!!!<h1>'
    return HttpResponse(s4)
