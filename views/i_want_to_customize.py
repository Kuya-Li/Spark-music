from core import controller

controllerClass = getattr(controller, "Controller")

# 我要定制
class I_want_to_customize(controllerClass):
    def __init__(self, config={}):
        """
        构造函数
        @param {Object} config 配置参数
        """
        config_init = {
            # 选择的模板那路径模板
            "tpl": "./i_want_to_customize/",
            # 选择的服务
            "services": "i_want_to_customize",
        }
        config_temp = config
        config_temp.update(config_init)
        super(I_want_to_customize , self).__init__(config_temp)

    # 添加数据成功后
    def Add_before(self, ctx):
        """
		添加数据前
		@param {Object} ctx http请求上下文
		@return {Object} 返回json-rpc格式结果
		"""
        body = ctx.body
        service = self.service
        # 计算
        result = service.Add(body, self.config)
        select = service.run("SELECT MAX(`i_want_to_customize_id`) AS max FROM `i_want_to_customize`")
        max = select[0]["max"]
        if max != None:
            ret = service.run("SELECT count(*) count FROM `customized_goods` INNER JOIN `i_want_to_customize` ON customized_goods.trade_name=i_want_to_customize.trade_name WHERE customized_goods.stock < i_want_to_customize.purchase_quantity AND i_want_to_customize.i_want_to_customize_id=" + str(max))
            if ret[0]["count"] > 0:
                service.run("DELETE FROM `i_want_to_customize` WHERE `i_want_to_customize_id`=" + str(max))
                return {
                        "code": 30000,
                        "message": "库存不足！"
                        }
        service.run("DELETE FROM `i_want_to_customize` WHERE `i_want_to_customize_id`=" + str(max))
        return {"code": 0}
    # 添加数据成功后
    def Add_after(self, ctx, result):
	    """
		添加数据前
		@param {Object} ctx http请求上下文
		@return {Object} 返回json-rpc格式结果
		"""
	    service = self.service
	    obj = service.Get_obj({}, {"orderby": "`i_want_to_customize_id` DESC"})
	    if obj:
	        # 计算
	        service.run("UPDATE `customized_goods` INNER JOIN `i_want_to_customize` ON customized_goods.trade_name=i_want_to_customize.trade_name SET customized_goods.stock= customized_goods.stock - i_want_to_customize.purchase_quantity WHERE i_want_to_customize.i_want_to_customize_id=" + str(obj["i_want_to_customize_id"]))
	    return result


