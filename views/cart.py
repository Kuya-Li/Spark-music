from core import controller

controllerClass = getattr(controller, "Controller")


# 购物车
class Cart(controllerClass):
    def __init__(self, config={}):
        """
        构造函数
        @param {Object} config 配置参数
        """
        config_init = {
            # 选择的模板那路径模板
            "tpl": "./cart/",
            # 选择的服务
            "services": "cart",
            # 唯一判断
            "unique": ["goods_id", "user_id"]
        }
        config_temp = config
        config_temp.update(config_init)
        super(Cart, self).__init__(config_temp)

    # 增
    def Add(self, ctx):
        """
		增
		@param {Object} ctx http请求上下文
		@return {Object} 返回json-rpc格式结果
		"""
        body = ctx.body
        unique = self.config.get("unique")
        obj = None
        qy = {}
        if unique:
            for i in range(len(unique)):
                key = unique[i]
                qy[key] = body.get(key)
            obj = self.service.Get_obj(qy)

        if obj:
            obj["num"] = obj["num"] + 1
            obj["price_count"] = obj["price"] * obj["num"]
            ret = self.service.Set(qy, obj, self.config)
            if not ret:
                return {"error": self.service.error}
            return {"result": ret}
        else:
            result = self.service.Add(body, self.config)
            if self.service.error:
                return {"error": self.service.error}
            return {"result": result}
