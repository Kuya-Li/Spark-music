from core import controller

controllerClass = getattr(controller, "Controller")


# 帮助方法,合并对象
def obj_update(*config):
    config_temp = {}
    for o in config:
        config_temp.update(o)
    return config_temp


# 订单
class Order(controllerClass):
    def __init__(self, config={}):
        """
        构造函数
        @param {Object} config 配置参数
        """
        config_init = {
            # 选择的模板那路径模板
            "tpl": "./order/",
            # 选择的服务
            "services": "order",
        }
        config_temp = config
        config_temp.update(config_init)
        super(Order, self).__init__(config_temp)

    # 首页
    def List(self, ctx):
        """列表页面
        @param {Object} ctx http请求上下文
        @return {Object} 返回html页面
        """
        query = dict(ctx.query)
        config_plus = {}
        if "field" in query:
            field = query.pop("field")
            config_plus["field"] = field
        if "page" in query:
            page = query.pop("page")
            config_plus["page"] = page
        if "size" in query:
            size = query.pop("size")
            config_plus["size"] = size

        # 文章列表
        result_list = self.service.Get_list(query, obj_update(self.config, config_plus))

        dict_t = {}
        for o in result_list:
            if o["order_number"]:
                if not (o["order_number"] in dict_t):
                    dict_t[o["order_number"]] = []
                dict_t[o["order_number"]].append(o)
        model = self.model(ctx, {"list": result_list, "dict": dict_t})
        return ctx.render(self.config["tpl"] + "list.html", model)


    def Get_business_order_list(self, ctx):
        query = dict(ctx.query)
        service = self.service
        if "user_id" in query:
            user_id = query.pop("user_id")
            sql1 = "SELECT *,t1.user_id as user_id FROM `order` t1 LEFT JOIN goods t2 ON t1.goods_id = t2.goods_id "
            sql1 += "WHERE t2.user_id = "+user_id
            sql2 = "SELECT count(t1.order_id) FROM `order` t1 LEFT JOIN goods t2 ON t1.goods_id = t2.goods_id "
            sql2 += "WHERE t2.user_id = "+user_id
            if "order_number" in query:
                order_number = query.pop("order_number")
                sql1 += " and t1.order_number like '%" + order_number +"%'"
                sql2 += " and t1.order_number like '%" + order_number +"%'"
            if "title" in query:
                title = query.pop("title")
                sql1 += " and t1.title like '%" + title +"%'"
                sql2 += " and t1.title like '%" + title +"%'"
            if "contact_name" in query:
                contact_name = query.pop("contact_name")
                sql1 += " and t1.contact_name like '%" + contact_name +"%'"
                sql2 += " and t1.contact_name like '%" + contact_name +"%'"
            if "state" in query:
                state = query.pop("state")
                sql1 += " and t1.state = '" + state +"'"
                sql2 += " and t1.state = '" + state +"'"
            if "page" in query:
                page = query.pop("page")
                if "size" in query:
                    size = query.pop("size")
                    if page and size:
                        sql1 += " limit "+str((int(page)-1)*int(size))+" , "+str(size)
            data1 = service.run(sql1)
            data2 = service.run(sql2)
            return {"result": {"list": data1, "count": data2}}
        return self.Get_list(ctx)

    def Get_list(self, ctx):
        """
        查多条
        @param {Object} ctx http请求上下文
        @return {Object} 返回json-rpc格式结果
        """
        query = dict(ctx.query)
        config_plus = {}
        if "field" in query:
            field = query.pop("field")
            config_plus["field"] = field
        if "page" in query:
            config_plus["page"] = query.pop("page")
        if "size" in query:
            config_plus["size"] = query.pop("size")
        if "orderby" in query:
            config_plus["orderby"] = query.pop("orderby")
        if "like" in query:
            config_plus["like"] = query.pop("like")
        if "groupby" in query:
            config_plus["groupby"] = query.pop("groupby")
        count = self.service.Count(query)
        lst = []
        if self.service.error:
            return {"error": self.service.error}
        elif count:
            lst = self.service.Get_list(query,
                                        obj_update(self.config, config_plus))
            resp = []
            for item in lst:
                item['buy_user_id'] = item['user_id']
                resp.append(item)
            if self.service.error:
                return {"error": self.service.error}
            self.interact_list(ctx, resp)


        return {"result": {"list": lst, "count": count}}