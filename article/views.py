from django.shortcuts import render,HttpResponse 
from .models import Article,User

# # Create your views here.
def add(request):
    user = User(name='作者2', password='password22')
    user.save()
    article = Article(title='第二篇文章', content='这是文章的内容。', author=user)
    article.save()
    return HttpResponse("添加文章成功")

def detail(request):
    article = Article.objects.first()
    return HttpResponse(f"第一篇文章的标题是: {article.title} 作者是: {article.author.name}")
    