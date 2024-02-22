from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from .models import Passanger, Vehicle, Book
from django.db import models
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.db.utils import IntegrityError

# Create your views here.

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    path = request.path
    method = request.method
    # return HttpResponse("Request path : {} and Request Method : {}".format(path, method))
    content=''' 
    <center><h2>Testing Django Request Response Objects</h2> 
    <p>Request path : " {}</p> 
    <p>Request Method :{}</p></center> 
    '''.format(path, method) 
    
    return HttpResponse(content)

def display_date(request):
    date_jointed = datetime.today()
    return HttpResponse(date_jointed)

def getUser(request):
    user = request.user
    return HttpResponse(user)

def pathview(request, name, id):
    return HttpResponse(f"Name : {name} and Id : {id}")

def qryview(request):
    name = request.GET['name']
    id = request.GET['id']
    
    return HttpResponse(f"Name : {name} and Id : {id}")

def showform(request): 
    return render(request, 'form.html')

@csrf_exempt
def book(request):
    if request.method == "GET":
        book = Book.objects.all().values()
        return JsonResponse({'book': list(book)})
    
    elif request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        
        book = Book(title=title, author=author, price=price)
    
        try:
            book.save()
        except IntegrityError:
            return JsonResponse({'error':'true','message':'required field missing'},status=400)

        return JsonResponse(model_to_dict(book), status=201)