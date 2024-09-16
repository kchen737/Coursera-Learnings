from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime

def home(request):
    return HttpResponse("<h1>Welcome to Hunan Wok</h1>")

def path(request):
    path = request.path
    return HttpResponse(path,content_type='text/html', charset='utf-8')

def say_hello(request):
    return HttpResponse("Hello World")

def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def menu(request):
    text = """<h1 style = "color: #F4CE14;"> Hi! This is Madison! </h1>
    <h2 style = "color: #FFA500" >This is Kaiming</h2>"""
    return HttpResponse(text)

def menuitems(request, dish):
    items = {
        'pasta': 'Pasta is a type of noodle made from combination of wheat or eggs',
        'falafel': 'Falfafel are deep fried patties'
        
    }
    description = items[dish]
    
    return HttpResponse(f"<h2> {dish} </h2>" + description)


''''
def myview(request):  

    if request.method=='GET':  
        pass
        #perform read or delete operation on the model  

    if request.method=='POST':  
        pass
        #perform insert or update operation on the model 
        
def myview(request): 
    if request.method=='GET': 
        val = request.GET['key'] 
        #perform read or delete operation on the model 
    if request.method=='POST': 
        val = request.POST['key'] 
        #perform insert or update operation on the model 
        
        
def myview(request):  

      if request.method=='GET':  
          pass
            #perform read or delete operation on the model  

      if request.method=='POST':  
            #perform insert or update operation on the model  
            context={ } #dict containing data to be sent to the client  

      return render(request, 'mytemplate.html', context) 
      
      '''