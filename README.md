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