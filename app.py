import importlib
import os
from subprocess import run

from flask import Flask, g, make_response, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from pyspark.sql import SparkSession

from core.middleware import middleware_check_permissions
from router import router

db = SQLAlchemy()
app = Flask(__name__, static_folder='static')
# 数据库链接配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@172.19.0.5:3306/CS866740_20220728155643'
app.secret_key = 'v&#prqo7t*(!ktb+8r=+83@#_$n1pg_xig$j=6v^r3#$i)wx87'
db.init_app(app)
app.config['UPLOAD_FOLDER'] = 'static/upload'
# 获得视图控制器路径
controller_dir = os.getcwd() + "/views"
# 模块绝对路径的数组
arr = []


def connect_db():
    connection = db.engine
    return connection


@app.before_request
def before_request():
    # 将链接池对象加入至flask全局对象里，用于mysqlpool使用
    g.db = connect_db()
    if request.method == "Origin" or request.method == "OPTIONS":
        resp = make_response()
        resp.status_code = 204
        resp.headers['Content-Type'] = "text/html; charset=utf-8"
        resp.headers['Access-Control-Allow-Origin'] = "*"
        # 允许你携带Content-Type请求头
        # 允许自定义前端可以添加请求头 token 字段
        resp.headers['Access-Control-Allow-Headers'] = "Content-Type,Accept,Authorization,x-auth-token"
        # 资格证书
        resp.headers["Access-Control-Allow-Credentials"] = "true"
        # 允许你发送DELETE,PUT
        resp.headers['Access-Control-Allow-Methods'] = "*"
        # 最大有效周期
        resp.headers["Access-Control-Max-Age"] = "86400"
        resp.status_code = 200
        return resp
    else:
        middleware_check_permissions()


@app.after_request
def after_request(response):
    g.db.dispose()
    return response


def foreach_file(path_name):
    for root, dirs, files in os.walk(path_name):
        for f in files:
            arr.append(os.path.join(root, f))


def load_module(f):
    # 将f变成相对路径
    route_path = (
        f.replace(controller_dir + "\\", "").replace(".py", "").replace("\\", "/")
    )
    # print(route_path)
    new_path = route_path.split('/')[-1]
    try:
        mod = importlib.import_module("views." + new_path)
        # print(mod)
        cs_controller = getattr(mod, new_path.capitalize())
        # controller是view文件夹下的内容
        controller = cs_controller()
        # 遍历出所有的controller的方法名（即action名）
        if route_path == "index":
            load_route(controller, "")
        else:
            load_route(controller, new_path)
    except Exception as e:
        print(e.args)


def load_route(controller, route_path):
    get = controller.config["get"]
    post = controller.config["post"]
    get_api = controller.config["get_api"]
    post_api = controller.config["post_api"]

    # 帮助函数 ，负责添加路由urlpatterns列表,其中controller是外部变量
    def append_urlpatterns(req_method, route_path_plus, action):
        print(route_path_plus)
        router_method = router(req_method, getattr(controller, action))
        app.add_url_rule("/" + route_path_plus, endpoint=route_path_plus + "_" + req_method, view_func=router_method,
                         methods=[req_method])

    if hasattr(controller, "Index"):
        append_urlpatterns("all", route_path, "Index")
    if hasattr(controller, "Api"):
        append_urlpatterns("all", "api" + "/" + route_path, "Api")
    for action in get:
        if action == "index":
            append_urlpatterns("get", action, action.capitalize())
        elif not route_path == "":
            append_urlpatterns("get", route_path + "/" + action, action.capitalize())
    for action in post:
        if action == "index":
            append_urlpatterns("post", action, action.capitalize())
        else:
            append_urlpatterns("post", route_path + "/" + action, action.capitalize())
    for action in get_api:
        if action == "index":
            append_urlpatterns("get", "api" + "/" + route_path, action.capitalize())
        else:
            append_urlpatterns("get", "api" + "/" + route_path + "/" + action, action.capitalize())

    for action in post_api:
        if action == "index":
            append_urlpatterns("post", "api" + "/" + route_path, action.capitalize())
        else:
            append_urlpatterns("post", "api" + "/" + route_path + "/" + action, action.capitalize())


foreach_file(controller_dir)

# 遍历模块数组，加载每个模块（内有加载路由）
for f in arr:
    if f.find(".pyc") == -1 and f.find("__init__") == -1:
        # pass
        load_module(f)


@app.route("/spark", methods=["post"])
def spark():
    params = request.get_json()
    spark = SparkSession \
        .builder \
        .appName("SparkByExamples.com") \
        .config("spark.sql.warehouse.dir", "/hive/warehouse/dir") \
        .config("hive.metastore.uris", "thrift://127.0.0.1:9083") \
        .enableHiveSupport() \
        .getOrCreate()

    return jsonify({})


@app.post("/hadoop")
def hadoop():
    params = request.get_json()
    if 'path' in params.keys():
        # 查询备份在hadoop下的表记录
        # path == 表名
        commod = f"hadoop fs -cat /user/hive/warehouse/{params['path']}/part-m-00000"
    else:
        # 查询hadoop目录下的文件夹
        # hadoop fs -chmod 777 /user/hive/warehouse/part-m-00000
        commod = "hadoop fs -ls /user/hive/warehouse"
    resp = run(commod, shell=True, universal_newlines=True, capture_output=True, text=True)
    stdout = resp.stdout.split('\n')
    data = []
    for i in stdout:
        if i != "":
            data.append(i)
    return jsonify(data)
# dataclass = HiveToMysql('CS866740_20220728155643')
# dataclass.init_hive_table()
# dataclass.init_hive_data()

if __name__ == '__main__':

    app.run(host="0.0.0.0", port=80)
