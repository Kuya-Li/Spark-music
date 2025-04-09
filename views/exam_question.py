from core import controller

controllerClass = getattr(controller, "Controller")


# 考试题目
class Exam_question(controllerClass):
    def __init__(self, config={}):
        """
        构造函数
        @param {Object} config 配置参数
        """
        config_init = {
            # 选择的模板那路径模板
            "tpl": "./exam_question/",
            # 选择的服务
            "services": "exam_question",
        }
        config_temp = config
        config_temp.update(config_init)
        super(Exam_question, self).__init__(config_temp)
