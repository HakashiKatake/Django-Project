from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello, world. You're at the DjangPractice home.")
    return render(request, 'website/index.html')



def about(request):
    #return HttpResponse("Hello, world. You're at the DjangPractice about.")
    return render(request, 'website/about.html')

def contact(request):
    #eturn HttpResponse("Hello, world. You're at the DjangPractice contact.")
    return render(request, 'website/contact.html')
