from core import controller

controllerClass = getattr(controller, "Controller")


# 错题
class User_answer_wrong(controllerClass):
    def __init__(self, config={}):
        """
        构造函数
        @param {Object} config 配置参数
        """
        config_init = {
            # 选择的模板那路径模板
            "tpl": "./user_answer_wrong/",
            # 选择的服务
            "services": "user_answer_wrong",
        }
        config_temp = config
        config_temp.update(config_init)
        super(User_answer_wrong, self).__init__(config_temp)
