from service import service_select
from core import controller

controllerClass = getattr(controller, "Controller")


# 帮助方法,合并对象
def obj_update(*config):
    config_temp = {}
    for o in config:
        config_temp.update(o)
    return config_temp


# 商品
class Goods(controllerClass):
    def __init__(self, config={}):
        """
        构造函数
        @param {Object} config 配置参数
        """
        config_init = {
            # 选择的模板那路径模板
            "tpl": "./goods/",
            # 选择的服务
            "services": "goods",
        }
        config_temp = config
        config_temp.update(config_init)
        super(Goods, self).__init__(config_temp)

    # 查一条
    def Get_obj(self, ctx):
        """
		查一条
		@param {Object} ctx http请求上下文
		@return {Object} 返回json-rpc格式结果
		"""
        query = dict(ctx.query)
        config_plus = {}
        if "field" in query:
            field = query.pop("field")
            config_plus["field"] = field

        obj = self.service.Get_obj(query, obj_update(self.config, config_plus))
        if self.service.error:
            return {"error": self.service.error}
        if obj:
            if obj["source_table"]:
                table = obj["source_table"]
                service = service_select(table)
                if service:
                    qy = {}
                    field = obj["source_field"]
                    qy[field] = obj["source_id"]
                    obj["info"] = service.Get_obj(qy)
            self.interact_obj(ctx, obj)
        return {"result": {"obj": obj}}
