# project
启动虚拟环境
source ./venv/bin/activate
关闭虚拟环境
deactivate
启动应用 
python3 manage.py rumserver 
stop应用
control + C 
新建一个app模块
python3 manage.py startapp appname
将类文件映射成数据库文件,需要在setting里面install app里加app名字
python3 manage.py makemigrations
数据库建表
python3 manage.py migrate


数据库:
filter   查询到符合条件的数据
exclude  排除掉符合条件的
get 只获取一条数据
1、exact 精准查询 
2、ieact 忽略大小写 数据库查询操作0839
3、contains包含 约等于 like '%key word%'
4、icontains 忽略带下写的包含关系
5、in  id_in = [1,2,3] 查出来id = 1和2和3的内容
6、gt id_gt = 4 查出来id > 4
7、gte id_gte = 4 查出来id >= 4 
8、lt
9、lte
10、startwith title_startwith='hello'
11、 istartwitth title_istartwith = 'hello' 忽略大小写
12、endwith 
13、iendwith 
14、range articles = Article.objects.filter(published_at__range=['2026-01-01','2026-01-30'])
15、date pub_date__date(2025,3,29)
16、year pub_date__year= 2025 pub_date__year_gte = 2025
17、month 
18、day
19、week_day 星期几
20、time 12:30:30
21、isnull  public_date__isnull=False 所有出版日期不为空的数据
22、regex 正则表达式 title_regex=r'^hello' 找出所有标题为hello开头的文章
23、iregex 大小写不敏感表达式
24、关联表查询: 复杂查询
SET FOREIGN_KEY_CHECKS = 0;  -- 关闭外键约束
TRUNCATE TABLE article_tag4_articles;
TRUNCATE TABLE article_tag4;
TRUNCATE TABLE article_art4;
SET FOREIGN_KEY_CHECKS = 1;  -- 恢复外键约束


