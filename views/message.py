from core import controller

controllerClass = getattr(controller, "Controller")


# 留言板
class Message(controllerClass):
    def __init__(self, config={}):
        """
        构造函数
        @param {Object} config 配置参数
        """
        config_init = {
            # 选择的模板那路径模板
            "tpl": "./message/",
            # 选择的服务
            "services": "message",
        }
        config_temp = config
        config_temp.update(config_init)
        super(Message, self).__init__(config_temp)
