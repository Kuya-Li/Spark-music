import os
import importlib

services_abspath_arr = []
services_arr = []
services_dir = os.getcwd() + "/services"


# print(services_dir)
# 遍历模块文件(绝对路径)加到services_abspath_arr数组


# 选择服务函数
def service_select(str):
    for service_item in services_arr:
        if str.capitalize() == service_item.__class__.__name__:
            return service_item


def foreach_file(path_name):
    for root, dirs, files in os.walk(path_name):
        for f in files:
            services_abspath_arr.append(os.path.join(root, f))


# 读取模块
# f:文件路径
def loadModule(f):
    # 将f变成相对路径
    f = f.replace(services_dir + "\\", "").replace(".py", "").replace("\\", "/")
    new_server_path = f.split('/')
    mod = importlib.import_module(
        "services." + new_server_path[-1]
    )
    arr_1 = f.split(".")
    cs_service = getattr(mod,new_server_path[-1].capitalize())
    # service的class形式
    service = cs_service()
    # print(services)
    services_arr.append(service)

foreach_file(services_dir)
for f in services_abspath_arr:
    if f.find(".pyc") == -1 and f.find("__init__") == -1:
        loadModule(f)
# print(services_arr)
