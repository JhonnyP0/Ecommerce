from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Items

#def store(request):
#    context= {}
#    return render(request,'store/store.html',context)

def cart(request):
    context= {}
    return render(request,'store/cart.html',context)

def store(request):
    myitems=Items.objects.all().values()
    template = loader.get_template('store/store.html')
    context={'myitems':myitems}
    return HttpResponse(template.render(context,request))

def dbtest(request):
    myitems=Items.objects.all().values()
    template = loader.get_template('store/dbtest.html')
    context={'myitems':myitems}
    return HttpResponse(template.render(context,request))