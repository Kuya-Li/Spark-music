from core.mysql import Service


# 订单
class Order(Service):
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
                "table": "order",
                # 分页大小
                "size": 10,
            }
        super(Order, self).__init__(config_temp)
