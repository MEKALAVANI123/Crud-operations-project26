from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
def display_topics(request):
    LOT=Topic.objects.all()
    LOT=Topic.objects.all()[1:]
    LOT=Topic.objects.filter(topic_name='cricket')
    d={'topics':LOT }
    return render(request,'display_topics.html',d)

def display_WebPage(request):
    LOW=WebPage.objects.all()
    LOW=WebPage.objects.filter(topic_name='cricket')
    LOW=WebPage.objects.filter(topic_name='Football')
    #LOW=WebPage.objects.get(topic_name='chess')
    LOW=WebPage.objects.all()[1:2:]
    LOW=WebPage.objects.all().order_by('name')


    LOW=WebPage.objects.all().order_by(Length('name'))
    #LOW=WebPage.objects.all()
    LOW=WebPage.objects.all().order_by(Length('name').desc())
    LOW=WebPage.objects.all()
    LOW=WebPage.objects.filter(name__startswith='k')
    LOW=WebPage.objects.filter(name__contains='S')
    LOW=WebPage.objects.filter(name__in=('virat','shreyas'))
    LOW=WebPage.objects.filter(name__regex='[a-zA-Z]{7}')
    LOW=WebPage.objects.filter(Q(topic_name='cricket') & Q(name='warner'))
    LOW=WebPage.objects.filter(Q(topic_name='cricket'))

    d={'WebPage':LOW}
    return render(request,'display_WebPage.html',d)

def display_AccessRecord(request):
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.filter(date__gt='2022-10-10')
    LOA=AccessRecord.objects.filter(date__gte='2022-10-10')
    LOA=AccessRecord.objects.filter(date__lt='2022-10-10')
    LOA=AccessRecord.objects.filter(date__lte='2022-10-10')
    LOA=AccessRecord.objects.filter(date__year='2020')
    LOA=AccessRecord.objects.filter(date__month='10')
    LOA=AccessRecord.objects.filter(date__day='5')
    LOA=AccessRecord.objects.filter(date__month__lt='10')





    d={'AccessRecord':LOA}
    return render(request,'display_AccessRecord.html',d)