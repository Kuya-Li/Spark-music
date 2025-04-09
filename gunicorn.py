# gunicorn.conf
daemon = True
workers = 4
threads = 2
bind = '0.0.0.0:80'
worker_class = 'uvicorn.workers.UvicornWorker'
# 设置最大并发量
worker_connections = 2000
# 设置进程文件目录
pidfile = '/opt/bitnami/flask/logs/gun.pid'
accesslog = '/opt/bitnami/flask/logs/gunicorn_acess.log'
errorlog = '/opt/bitnami/flask/logs/gunicorn_error.log'
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'
loglevel = 'debug'
