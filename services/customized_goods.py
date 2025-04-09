from core.mysql import Service


# 定制商品服务
class Customized_goods(Service):
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
                "table": "customized_goods",
                # 分页大小
                "size": 30,
                "page": 1,
            }
        super(Customized_goods , self).__init__(config_temp)
