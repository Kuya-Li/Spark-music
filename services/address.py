from core.mysql import Service


# 收货地址
class Address(Service):
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
                "table": "address",
                # 分页大小
                "size": 10,
            }
        super(Address, self).__init__(config_temp)
