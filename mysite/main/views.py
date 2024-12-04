from django.shortcuts import render
from .models import News


def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def services(request):
    return render(request, 'main/services.html')

def contact(request):
    return render(request, 'main/contact.html')

def news_view(request):
    news_list = News.objects.all().order_by('-created_at')  # Fetch all news articles ordered by creation date
    return render(request, 'main/news.html', {'news_list': news_list})