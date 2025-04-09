from core.mysql import Service


# 网站公告服务
class Website_announcement(Service):
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
                "table": "website_announcement",
                # 分页大小
                "size": 30,
                "page": 1,
            }
        super(Website_announcement , self).__init__(config_temp)
