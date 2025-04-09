from core.mysql import Service


# 考试答题
class User_answer(Service):
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
                "table": "user_answer",
                # 分页大小
                "size": 10,
            }
        super(User_answer, self).__init__(config_temp)
