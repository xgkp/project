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
2、ieact 忽略大小写