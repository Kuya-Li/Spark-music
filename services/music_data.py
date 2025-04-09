from core.mysql import Service


# 音乐数据服务
class Music_data(Service):
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
                "table": "music_data",
                # 分页大小
                "size": 30,
                "page": 1,
            }
        super(Music_data , self).__init__(config_temp)
