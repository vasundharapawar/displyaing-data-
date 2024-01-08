from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse
def display_topics(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'display_topics.html',d)


def display_webpages(request):
    QLWO=Webpage.objects.all()
    d={'webpages':QLWO}
    return render(request,'display_webpages.html',d)



def insert_topic(request):
    tn=input('enter topic Name')

    NTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NTO.save()

    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'display_topics.html',d)


def insert_webpage(request):
    tn=input('enter tn')
    n=input('enter name')
    u=input('enter url')
    e=input('enter email')

    TO=Topic.objects.get(topic_name=tn)

    NWO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
    NWO.save()

    return HttpResponse('Webpage is created')

def update_Webpage(request):
   QLWO=Webpage.objects.all()
   Webpage.objects.filter(pk=5).update(topic_name='football')
   d={'webpage':QLWO}
   return render(request,'display_webpages.html',d)

    












































