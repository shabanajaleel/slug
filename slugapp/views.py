from django.shortcuts import render
from . models import *
context={}

# Create your views here.
def fnhome(request):
    articles=Article.objects.all()
    context['articles']=articles
    if request.method=="POST":
        name=request.POST.get('name')
        author=request.POST.get('author')
        description=request.POST.get('description')

        article=Article.objects.get_or_create(Name=name,Author=author,Description=description)
    return render(request,'add_article.html',context)

def fnviewbook(request,slug):
    articles=Article.objects.get(article_slug=slug)
    context['article']=articles
    return render(request,'view_book.html',context)