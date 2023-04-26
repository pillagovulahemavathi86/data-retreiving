from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.functions import Length



# Create your views here.
from django.db.models import Q
from app.models import *
def display_topics(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    LOW=Webpage.objects.all()
    #LOW=Webpage.objects.get(topic_name='coco')
    LOW=Webpage.objects.filter(name='neha')
    LOW=Webpage.objects.exclude(topic_name='cricket')
    LOW=Webpage.objects.get(name='neha')
    LOW=Webpage.objects.order_by('name')
    LOW=Webpage.objects.order_by('-name')
    LOW=Webpage.objects.order_by(Length('url'))
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(url__endswith='in')
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(name__in=('arun','neha'))
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(Q(topic_name='cricket')&Q(name='kohli'))
    LOW=Webpage.objects.filter(Q(topic_name='cricket')|Q(name='kohli'))
    
    
    d={'webpages':LOW}
    return render(request,'display_webpages.html',d)

def display_accessrecords(request):
    LOA=Accessrecords.objects.all()
    LOA=Accessrecords.objects.filter(date__gt='2022-10-10')
    LOA=Accessrecords.objects.all()
    LOA=Accessrecords.objects.filter(date__year='2022')
    LOA=Accessrecords.objects.all()
    LOA=Accessrecords.objects.filter(date__month='2')
    LOA=Accessrecords.objects.all()
    LOA=Accessrecords.objects.filter(date__day='19')
    LOA=Accessrecords.objects.all()
    LOA=Accessrecords.objects.filter(date__year__gt='1997')
    LOA=Accessrecords.objects.filter(date__day__lt='20')
    LOA=Accessrecords.objects.all()
    LOA=Accessrecords.objects.filter(author__startswith='s')
    
    
    

    d={'access':LOA}
    return render(request,'display_accessrecords.html',d)

