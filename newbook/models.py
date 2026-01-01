from django.db import models

class NewBook(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    published_date = models.DateField(auto_now_add=True)
    price = models.FloatField(default=0.0)
    # other = models.AutoField(primary_key=True) # 自动增长的主键字段
    # other2 = models.BigAutoField(primary_key=True) # 大整数自动增长的主键字段
    # other3 = models.ImageField to='images/'  # 图片字段，上传到media/images/目录下 图片
    # other4 = models.FileField(upload_to='files/')  # 文件字段，上传到media/files/目录下 文件
    # other5 = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # 十进制字段，适合存储货币等精确数值
    # other6 = models.UUIDField(auto_created=True, unique=True)  # UUID字段，存储唯一标识符
    # other7 = models.DateTimeField(auto_now=True)  # 日期时间字段，自动设置为当前时间
    # other8 = models.TimeField(auto_now_add=True)  # 时间字段，自动设置为当前时间
    # other9 = models.BinaryField()  # 二进制字段，存储二进制数据
    # other10 = models.SlugField(max_length=50, unique=True)  # Slug字段，适合用于URL中的标识符
    # other11 = models.JSONField(default=dict)  # JSON字段，存储JSON格式的数据
    # other12 = models.EmailField(max_length=254, unique=True)  # 邮箱字段，存储电子邮件地址
    # other13 = models.URLField(max_length=200)  # URL字段，存储网址
    # other14 = models.BooleanField(default=True)  # 布尔字段，存储True/False值
    # other15 = models.IntegerField(default=0)  # 整数字段，存储整数值
    # other16 = models.FloatField(default=0.0)  # 浮点数字段，存储浮点数值
    # other17 = models.TextField()  # 文本字段，存储大段文本内容
    # other18 = models.CharField(max_length=255)  # 字符字段，存储短文本内容
    # other19 = models.SmallIntegerField(default=0)  # 小整数字段，存储较小范围的整数值
    # other20 = models.PositiveIntegerField(default=0)  # 正整数字段，存储非负整数值
    # other21 = models.PositiveSmallIntegerField(default=0)  # 正小整数字段，存储非负小范围整数值

class Author(models.Model):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=100)
    datejoined = models.DateField(auto_now_add=True)
    visitcount = models.BigIntegerField(default=0)
    profile = models.TextField()
    website = models.URLField()
    age = models.IntegerField(default=0)
    email = models.EmailField()

 