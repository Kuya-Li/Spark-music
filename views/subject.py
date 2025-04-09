from core import controller

controllerClass = getattr(controller, "Controller")


# 科目
class Subject(controllerClass):
    def __init__(self, config={}):
        """
        构造函数
        @param {Object} config 配置参数
        """
        config_init = {
            # 选择的模板那路径模板
            "tpl": "./subject/",
            # 选择的服务
            "services": "subject",
        }
        config_temp = config
        config_temp.update(config_init)
        super(Subject, self).__init__(config_temp)
