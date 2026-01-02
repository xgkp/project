from django.shortcuts import render,HttpResponse 
from .models import Article,User,Art2,Usr2

# # Create your views here.
def add(request):
    user = User.objects.get(id=2)
    article = Article(title='第三篇文章', content='这是第三篇文章的内容。', author=user)
    article.save()
    return HttpResponse("添加文章成功")

def detail(request):
    article = Article.objects.first()
    return HttpResponse(f"第一篇文章的标题是: {article.title} 作者是: {article.author.name}")
    
def one_to_more(request):
    user = User.objects.get(id=2)
    articles = user.article_set.all()
    return HttpResponse(f"用户 {user.name} 的文章有: {[article.title for article in articles]}")

def adda2(request):
    user1 = Usr2(name='用户1', password='pwd1')
    user2 = Usr2(name='用户2', password='pwd2')
    user1.save()
    user2.save()
    article1 = Art2(title='第一篇文章', content='这是第一篇文章的内容。', author=user1)
    article2 = Art2(title='第二篇文章', content='这是第二篇文章的内容。', author=user2)
    article3 = Art2(title='第三篇文章', content='这是第三篇文章的内容。', author=user2)
    article1.save()
    article2.save()
    article3.save()
    return HttpResponse("添加文章成功")

def detaila2(request):
    usr2 = Usr2.objects.get(id=6)
    articles = usr2.articles.filter(title__contains='第').all()
    for article in articles:
        print(f"文章标题: {article.title} 作者: {article.author.name}")
    # 在这里能用articles因为在Art2的author属性foreignkey里的related_name='articles'
    return HttpResponse(f"success")

def query1exact(request):
    article = Art2.objects.filter(title__exact='第一篇文章')
    print(str(article.query))
    for article in article: 
        print(f"文章标题: {article.title} 作者: {article.author.name}")
    return HttpResponse(f"success")
    # 我这里需要print(str(article.query))
    