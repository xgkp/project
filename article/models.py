from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True,null=True)
    # 外键,级别联删除
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Usr2(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Art2(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # 外键,级别联删除
    author = models.ForeignKey(Usr2, on_delete=models.CASCADE, related_name='articles')

class Comment(models.Model):
    content = models.TextField()
    origin_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)



class Usr3(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Usr3Extend(models.Model):
    nickname = models.TextField()
    email = models.EmailField()
    user = models.OneToOneField(Usr3, on_delete=models.CASCADE)


class Art4(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

class Tag4(models.Model):
    name = models.CharField(max_length=50)
    articles = models.ManyToManyField(to='Art4',related_name="articles")  # 多对多关系
    # 标签跟文章是多对多的关系
    # 这里课程里面的articles应该改为tags更合适

    
