from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category
 

def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'список новостей',
    }
    return render(request, 'news/index.html', context)

def test(request):
    return HttpResponse("test url")

def get_category(request, index_category):
    news = News.objects.filter(category_id=index_category)
    category = Category.objects.get(pk=index_category)
    return render(request, 'news/category.html', {'news': news, 'category': category})
