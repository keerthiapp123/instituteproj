from django.shortcuts import render
from .models import ServisesData
from .models import FeedbackData

# Create your views here.
def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def servises(request):
    sd=ServisesData.objects.all()
    return render(request,'servises.html',{'sd':sd})

def feedback(request):
    if request.method=='GET':
        fd=FeedbackData.objects.all()
        return render(request,'feedback.html',{'fd':fd})
    else:
        fd=FeedbackData(
            name=request.POST.get('name'),
            ratings=request.POST.get('ratings'),
            comments=request.POST.get('comments')
        ).save()
        fd=FeedbackData.objects.all()
        return render(request,'feedback.html',{'fd':fd})






def gallery(request):
    return render(request,'gallery.html')