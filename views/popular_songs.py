from core import controller
import numpy as np

controllerClass = getattr(controller, "Controller")

# 热门歌曲
class Popular_songs(controllerClass):
    def __init__(self, config={}):
        """
        构造函数
        @param {Object} config 配置参数
        """
        config_init = {
            # 选择的模板那路径模板
            "tpl": "./popular_songs/",
            # 选择的服务
            "services": "popular_songs",
        }
        config_temp = config
        config_temp.update(config_init)
        super(Popular_songs , self).__init__(config_temp)

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

    # 协同过滤算法
    def Get_hits_list(self, ctx):
        query = dict(ctx.query)
        service = self.service
        if "user_id" in query:
            user_id = query.pop("user_id")
            if user_id == '':
                return self.Get_list(ctx)
            else:
                # 查询该用户常点击
                hitsSource = "SELECT COUNT( hits_id ) AS hits_count, source_id FROM hits WHERE source_table = 'popular_songs' AND user_id = " + user_id + " GROUP BY source_id"
                hitsSourceList = service.run(hitsSource)
                # 判断是否为空,代表当前用户暂无点击数据，那么取其他用户的最常点击
                if len(hitsSourceList) <= 0:
                    hitsSource = "SELECT COUNT( hits_id ) AS hits_count, source_id FROM hits WHERE source_table = 'popular_songs' GROUP BY source_id"
                    hitsSourceList = service.run(hitsSource)
                # 二次处理-如果依旧为空则取添加时间前12条数据
                if len(hitsSourceList) <= 0:
                    sql = "SELECT * FROM popular_songs ORDER BY create_time DESC LIMIT 0,12"
                    list = service.run(sql)
                    return {"result": {"list": list, "count": len(list)}}
                else:
                    # 对用户点击量进行排序取得最大值
                    max = 0
                    maxSourceId = 0
                    for o in hitsSourceList:
                        hitsCount = o["hits_count"]
                        if hitsCount > max:
                            max = hitsCount
                            maxSourceId = o["source_id"]
                    # 查询该用户点击最大值的种类
                    typeSql = "SELECT music_genre FROM popular_songs WHERE popular_songs_id = " + str(
                        maxSourceId)
                    typeList = service.run(typeSql)
                    # 如果为空则取添加时间前12条数据
                    if len(typeList) <= 0:
                        sql = "SELECT * FROM popular_songs ORDER BY create_time DESC LIMIT 0,12"
                        list = service.run(sql)
                        return {"result": {"list": list, "count": len(list)}}
                    else:
                        # 查询该种类的数据
                        typeName = typeList[0]["music_genre"]
                        sql = "SELECT * FROM popular_songs WHERE music_genre = '" + typeName + "'"
                        resultList = service.run(sql)
                        # 如果为空则取添加时间前12条数据
                        if len(resultList) <= 0:
                            sql = "SELECT * FROM popular_songs ORDER BY create_time DESC LIMIT 0,12"
                            list = service.run(sql)
                            return {"result": {"list": list, "count": len(list)}}
                        else:
                            # 对结果排序-冒泡排序
                            n = len(resultList)
                            for i in range(n):
                                # 是否发生交换
                                swapped = False
                                for j in range(n - i - 1):
                                    if resultList[j]["hits"] < resultList[j + 1]["hits"]:
                                        resultList[j], resultList[j + 1] = resultList[j + 1], resultList[j]
                                        swapped = True
                                if not swapped:
                                    # 没有发生交换，则说明数组已有序,停止冒泡
                                    break
                            if len(resultList) < 12:
                                # 判断是否有12条-如果不足则计算其他类型和用户当前点击最多的余弦相似度，依次往下取得数据
                                typeCosSql = "SELECT music_genre FROM popular_songs WHERE music_genre <> '" + typeName + "' GROUP BY music_genre"
                                typeCosList = service.run(typeCosSql)
                                if len(typeCosList) > 0:
                                    for o in typeCosList:
                                        o["cosSim"] = self.similar(typeName, o["music_genre"], 2)
                                    # 冒泡根据相似度排序
                                    cosn = len(typeCosList)
                                    for i in range(cosn):
                                        # 是否发生交换
                                        swapped = False
                                        for j in range(n - i - 1):
                                            if typeCosList[j]["cosSim"] < typeCosList[j + 1]["cosSim"]:
                                                typeCosList[j], typeCosList[j + 1] = typeCosList[j + 1], typeCosList[j]
                                                swapped = True
                                        if not swapped:
                                            # 没有发生交换，则说明数组已有序,停止冒泡
                                            break
                                    # 逐条加入数据
                                    for o in typeCosList:
                                        sql = "SELECT * FROM popular_songs WHERE music_genre = '" + o["music_genre"] + "' ORDER BY create_time DESC LIMIT 0," + str(12 - len(resultList))
                                        list = service.run(sql)
                                        if len(list) > 0:
                                            resultList.extend(list)
                            return {"result": {"list": resultList, "count": len(resultList)}}
        return self.Get_list(ctx)

    # 计算余弦相似度
    def similar(self, s, t, f):
        print(s)
        print(t)
        if not s or not t:
            return 0
        if s == t:
            return 100
        if len(s) > len(t):
            l = len(s)
        else:
            l = len(t)
        n = len(s)
        m = len(t)
        d = np.zeros((n+1, m+1))
        if not f:
            f = 2

        def min(a, b, c):
            if a < b:
                if a < c:
                    return a
                else:
                    return c
            else:
                if b < c:
                    return b
                else:
                    return c

        if n == 0:
            return m
        if m == 0:
            return n
        for i in range(0, n+1, 1):
            d[i][0] = i
        for j in range(0, m+1, 1):
            d[0][j] = j
        for i in range(1, n+1, 1):
            si = s[i - 1: i]
            for j in range(1, m+1, 1):
                tj = t[j - 1: j]
                if si == tj:
                    cost = 0
                else:
                    cost = 1
                d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + cost)
        res = (1 - d[n][m] / l) * 100
        return "{:.2f}".format(res)



