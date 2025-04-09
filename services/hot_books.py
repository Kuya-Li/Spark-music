from core.mysql import Service


# 热卖图书服务
class Hot_books(Service):
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
                "table": "hot_books",
                # 分页大小
                "size": 30,
                "page": 1,
            }
        super(Hot_books , self).__init__(config_temp)
