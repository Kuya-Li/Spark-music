from core import controller

controllerClass = getattr(controller, "Controller")


# 收货地址
class Address(controllerClass):
    def __init__(self, config={}):
        """
        构造函数
        @param {Object} config 配置参数
        """
        config_init = {
            # 选择的模板那路径模板
            "tpl": "./address/",
            # 选择的服务
            "services": "address",
        }
        config_temp = config
        config_temp.update(config_init)
        super(Address, self).__init__(config_temp)
