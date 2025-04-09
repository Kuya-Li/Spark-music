from core.mysql import Service


# 热门歌曲服务
class Popular_songs(Service):
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
                "table": "popular_songs",
                # 分页大小
                "size": 30,
                "page": 1,
            }
        super(Popular_songs , self).__init__(config_temp)
