from core import controller

controllerClass = getattr(controller, "Controller")


# 答题
class Subject_user_answer(controllerClass):
    def __init__(self, config={}):
        """
        构造函数
        @param {Object} config 配置参数
        """
        config_init = {
            # 选择的模板那路径模板
            "tpl": "./subject_user_answer/",
            # 选择的服务
            "services": "subject_user_answer",
        }
        config_temp = config
        config_temp.update(config_init)
        super(Subject_user_answer, self).__init__(config_temp)
