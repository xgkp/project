from django.shortcuts import render,HttpResponse 
from .models import Art4, Article, Tag4,User,Art2,Usr2

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
    

def addrange(request):
    user = User(name='用户3', password='pwd3')
    user.save()
    article = Article(title='第三篇文章', content='这是第三篇文章的内容。', author=user)
    article.save()
    return HttpResponse("添加文章成功")

def searchrange(request):
    articles = Article.objects.filter(published_at__range=['2026-01-01','2026-01-30'])
    print(str(articles.query))
    print("查询结果:")
    print(articles)
    for article in articles:
        print(f"文章标题: {article.title} 发布时间: {article.published_at}")
    return HttpResponse("查询成功")


def addtag4andart4(request):
    tag1 = Tag4(name='科技')
    tag2 = Tag4(name='健康')
    tag3 = Tag4(name='教育')
    tag1.save()
    tag2.save()
    tag3.save()
    article1 = Art4(title='科技的未来', content='科技正在改变世界。')
    article2 = Art4(title='健康生活', content='保持健康的生活方式。')
    article3 = Art4(title='教育的重要性', content='教育是社会进步的基石。')
    article4 = Art4(title='科技与健康', content='科技如何促进健康。')
    article5 = Art4(title='教育科技', content='科技在教育中的应用。')
    article6 = Art4(title='未来教育', content='未来的教育将会怎样。')
    article1.save()
    article2.save()
    article3.save()     
    article4.save()
    article5.save()
    article6.save()
    # 为文章添加标签
    article1.articles.add(tag1)
    article2.articles.add(tag2)
    article3.articles.add(tag3)
    article4.articles.add(tag1, tag2)
    article5.articles.add(tag1, tag3)
    article6.articles.add(tag3)
    return HttpResponse("添加文章和标签成功")

def querytag4andart4(request):
    tag = Tag4.objects.get(id=3)
    articles = tag.articles.all()
    print(f"标签 '{tag.name}' 关联的文章有:")
    for article in articles:
        print(f"文章标题: {article.title}")
    return HttpResponse("查询标签和文章成功")

def query44(request):
    tags = Tag4.objects.filter(articles__title__contains='科技') 
    print(str(tags.query))
    print("标题包含'科技'的文章有:")
    for tag in tags:
       print(f"标签名称: {tag.name}")  
    return HttpResponse("查询包含'科技'标签的文章成功")

    


    