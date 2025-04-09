from core import controller

controllerClass = getattr(controller, "Controller")


# 广告
class Access_token(controllerClass):
    def __init__(self, config={}):
        """
        构造函数
        @param {Object} config 配置参数
        """
        config_init = {
            # 选择的模板那路径模板
            "tpl": "./access_token/",
            # 选择的服务
            "services": "access_token",
        }
        config_temp = config
        config_temp.update(config_init)
        super(Access_token, self).__init__(config_temp)