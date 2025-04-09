from core import controller

controllerClass = getattr(controller, "Controller")


# 友情链接
class Link(controllerClass):
    def __init__(self, config={}):
        """
        构造函数
        @param {Object} config 配置参数
        """
        config_init = {
            # 选择的模板那路径模板
            "tpl": "./link/",
            # 选择的服务
            "services": "link",
        }
        config_temp = config
        config_temp.update(config_init)
        super(Link, self).__init__(config_temp)
