from core.mysql import Service


# 题库
class Exam_question_database(Service):
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
                "table": "exam_question_database",
                # 分页大小
                "size": 10,
            }
        super(Exam_question_database, self).__init__(config_temp)
