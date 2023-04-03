from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.models import *
def insert_Topic(request):
    tn=input('enter the Topic_name:')
    To=Topic.objects.get_or_create(topic_name=tn)[0]
    To.save()
    return HttpResponse('topic_name is inserted')
def insert_Webpage(request):
    tn=input('enter the Topic_name:')
    n=input('enter the name:')
    url=input('enter the url:')
    To=Topic.objects.get_or_create(topic_name=tn)[0]
    To.save()
    Wo=Webpage.objects.get_or_create(topic_name=To,name=n,url=url)[0]
    Wo.save()
    return HttpResponse('inserted successfully')
def insert_AccessRecord(request):
    tn=input('enter the Topic_name')
    n=input('enter the name:')
    url=input('enter the url:')
    author=input('enter the author')
    date=input('enter the date')
    To=Topic.objects.get_or_create(topic_name=tn)[0]
    To.save()
    Wo=Webpage.objects.get_or_create(topic_name=To,name=n,url=url)[0]
    Wo.save()
    Ao=AccessRecord.objects.get_or_create(name=Wo,author=author,date=date)[0]
    Ao.save()
    return HttpResponse('inserted successfully')
