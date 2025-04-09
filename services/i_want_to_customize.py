from core.mysql import Service


# 我要定制服务
class I_want_to_customize(Service):
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
                "table": "i_want_to_customize",
                # 分页大小
                "size": 30,
                "page": 1,
            }
        super(I_want_to_customize , self).__init__(config_temp)
