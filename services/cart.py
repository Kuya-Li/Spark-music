from core.mysql import Service


# 购物车
class Cart(Service):
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
                "table": "cart",
                # 分页大小
                "size": 10
            }
        super(Cart, self).__init__(config_temp)
