from core.mysql import Service


# 音乐信息服务
class Music_information(Service):
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
                "table": "music_information",
                # 分页大小
                "size": 30,
                "page": 1,
            }
        super(Music_information , self).__init__(config_temp)
