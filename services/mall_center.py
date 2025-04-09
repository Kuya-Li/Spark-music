from core.mysql import Service


# 商城中心服务
class Mall_center(Service):
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
                "table": "mall_center",
                # 分页大小
                "size": 30,
                "page": 1,
            }
        super(Mall_center , self).__init__(config_temp)
