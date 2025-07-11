from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

# Create your views here.


def home(request):
    return HttpResponse("Hello, world! This is the home page.")

def back(request):
    return render(request, 'background.html')

def henish(request):
    return HttpResponse("henish rabari jantral")

def rs(request):
    return render(request, 'frist.html')


def demo(request):

    peoples = [
        {'name': 'kavy', 'age': 17},
        {'name': 'henish', 'age': 18},
        {'name': 'jay', 'age': 28},
        {'name': 'aryan', 'age': 35},
    ]

    for people in peoples:
        print(people)

    
    return render(request, 'demo.html',context= {'peoples': peoples})

def demo1(request):

    tables = [
    {'name' :'A.C','price' : 50000},
    {'name' :'FEN','price' : 6000},
    {'name' :'TEBLE FEN','price' : 4000},
    {'name' :'WOSHING MASHIN','price' : 30000},
    {'name' :'MOBAILE','price' : 20000},
    {'name' :'T.V','price' : 35000},
    {'name' :'FREEZ','price' : 15000},
    {'name' :'BED','price' : 10000},
    {'name' :'BIKE,BULLETE','price' : 250000}
    ]
    for  table in tables:
        print(table)

    return render(request,"demo11.html",context={"tables": tables})

                                                                                                                                                                                                                                                                                                                                    