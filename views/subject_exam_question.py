from core import controller

controllerClass = getattr(controller, "Controller")


# 试题
class Subject_exam_question(controllerClass):
    def __init__(self, config={}):
        """
        构造函数
        @param {Object} config 配置参数
        """
        config_init = {
            # 选择的模板那路径模板
            "tpl": "./subject_exam_question/",
            # 选择的服务
            "services": "subject_exam_question",
        }
        config_temp = config
        config_temp.update(config_init)
        super(Subject_exam_question, self).__init__(config_temp)
