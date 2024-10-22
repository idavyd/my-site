from django.shortcuts import render
from django.http import HttpResponse
import time

# Create your views here.
def home_view(request, *args,**kwargs):
    return render(request,'home.html', {})

def about_view(request, *args,**kwargs):
    my_context = {
        'my_text': 'This is about text',
        'my_number': 123,
        'my_list': ['Nvidia Video Card', 'Intel Processor', 'AMD videocard']
    }
    #return HttpResponse('<h1>Hello Wolrd</h1>')
    return render(request,'about.html', my_context)

def contact_view(request):
    print(f'{request.user} opened contact page')
    print(request.path)
    return render(request,'contact.html',{})





