from core import controller

controllerClass = getattr(controller, "Controller")

# 普通用户
class Regular_users(controllerClass):
    def __init__(self, config={}):
        """
        构造函数
        @param {Object} config 配置参数
        """
        config_init = {
            # 选择的模板那路径模板
            "tpl": "./regular_users/",
            # 选择的服务
            "services": "regular_users",
        }
        config_temp = config
        config_temp.update(config_init)
        super(Regular_users , self).__init__(config_temp)

    # 添加数据成功后
    def Add_before(self, ctx):
        """
		添加数据前
		@param {Object} ctx http请求上下文
		@return {Object} 返回json-rpc格式结果
		"""
        body = ctx.body
        service = self.service
        return {"code": 0}



