from django.shortcuts import render
from .models import Article
# Create your views here.
def index(request):
  articles = Article.objects.all()
  words = {
    'msg':'確認の表示',
    'articles':articles,
  }
  return render(request, 'blog/index.html', words)