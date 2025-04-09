from core import controller

controllerClass = getattr(controller, "Controller")


# 题库
class Exam_question_database(controllerClass):
    def __init__(self, config={}):
        """
        构造函数
        @param {Object} config 配置参数
        """
        config_init = {
            # 选择的模板那路径模板
            "tpl": "./exam_question_database/",
            # 选择的服务
            "services": "exam_question_database",
        }
        config_temp = config
        config_temp.update(config_init)
        super(Exam_question_database, self).__init__(config_temp)
