from django.shortcuts import render
from .models import Article
# Create your views here.
def index(request):
  article = Article.objects.order_by('-pub_date')[0] 
  words = {
    'msg':'確認の表示',
    'article':article,
  }
  return render(request, 'blog/index.html', words)

def menu(request):
  return render(request, 'blog/menu.html',)

def access(request):
  return render(request, 'blog/access_SNS.html',)

def line(request):
  return render(request, 'blog/LINE.html',)

