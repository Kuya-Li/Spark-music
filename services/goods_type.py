from core.mysql import Service


# 商品分类
class Goods_type(Service):
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
                "table": "goods_type",
                # 分页大小
                "size": 10,
            }
        super(Goods_type, self).__init__(config_temp)
