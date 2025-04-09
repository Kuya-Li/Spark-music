from core.mysql import Service


# 科目
class Subject(Service):
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
                "table": "subject",
                # 分页大小
                "size": 10,
            }
        super(Subject, self).__init__(config_temp)
