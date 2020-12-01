from django.shortcuts import render

# Create your views here.
def index(request):
  words = {
    'msg':'確認の表示'
  }
  return render(request, 'blog/index.html', words)