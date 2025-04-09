from service import service_select
from core import controller

controllerClass = getattr(controller, "Controller")


# 帮助方法,合并对象
def obj_update(*config):
    config_temp = {}
    for o in config:
        config_temp.update(o)
    return config_temp


# 商品分类
class Goods_type(controllerClass):
    def __init__(self, config={}):
        """
        构造函数
        @param {Object} config 配置参数
        """
        config_init = {
            # 选择的模板那路径模板
            "tpl": "./goods_type/",
            # 选择的服务
            "services": "goods_type",
        }
        config_temp = config
        config_temp.update(config_init)
        super(Goods_type, self).__init__(config_temp)
