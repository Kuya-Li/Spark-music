from core.mysql import Service


# 考试题目
class Exam_question(Service):
    def __init__(self, *config):
        """
        构造函数
        @param {Object} config 配置参数
        """
        if config:
            config_temp = config[0]
        else:
            config_temp = {
                # 操作的表
                "table": "exam_question",
                # 分页大小
                "size": 10,
            }
        super(Exam_question, self).__init__(config_temp)
