from core.mysql import Service


# 错题
class User_answer_wrong(Service):
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
                "table": "user_answer_wrong",
                # 分页大小
                "size": 10,
            }
        super(User_answer_wrong, self).__init__(config_temp)
