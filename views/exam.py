from core import controller

controllerClass = getattr(controller, "Controller")


# 考试
class Exam(controllerClass):
    def __init__(self, config={}):
        """
        构造函数
        @param {Object} config 配置参数
        """
        config_init = {
            # 选择的模板那路径模板
            "tpl": "./exam/",
            # 选择的服务
            "services": "exam",
        }
        config_temp = config
        config_temp.update(config_init)
        super(Exam, self).__init__(config_temp)
