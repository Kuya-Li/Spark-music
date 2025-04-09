from core import controller
import numpy as np

controllerClass = getattr(controller, "Controller")

# 热卖图书
class Hot_books(controllerClass):
    def __init__(self, config={}):
        """
        构造函数
        @param {Object} config 配置参数
        """
        config_init = {
            # 选择的模板那路径模板
            "tpl": "./hot_books/",
            # 选择的服务
            "services": "hot_books",
        }
        config_temp = config
        config_temp.update(config_init)
        super(Hot_books , self).__init__(config_temp)

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
    # 随机生成一个m x n的用户-物品矩阵，值在[0, 5]之间，0表示未点击过
    m = 10
    n = 20
    R = np.random.randint(6, size=(m, n))

    # 计算相似度矩阵，使用皮尔逊相关系数作为相似度度量
    def similarity_matrix(R):
        m, n = R.shape
        # 创建一个n x n的相似度矩阵
        sim_matrix = np.zeros((n, n))
        for i in range(n):
            for j in range(i + 1, n):
                # 找到同时评价过物品i和物品j的用户，计算它们之间的相似度
                idx = (R[:, i] > 0) & (R[:, j] > 0)
                if np.sum(idx) > 0:
                    sim_matrix[i, j] = np.corrcoef(R[idx, i], R[idx, j])[0, 1]
                    sim_matrix[j, i] = sim_matrix[i, j]
        return sim_matrix

    # 预测用户对物品的点击，使用加权平均值作为预测值
    def predict_rating(user_id, item_id, R, sim_matrix, k=3):
        n = R.shape[1]
        # 找到和物品item_id最相似的k个物品，计算它们和用户user_id评分的加权平均值
        sim_scores = sim_matrix[item_id, :]
        idx = (R[user_id, :] > 0) & (sim_scores > 0)
        if np.sum(idx) == 0:
            return 0
        sim_scores = sim_scores[idx]
        ratings = R[user_id, idx]
        if len(sim_scores) > k:
            idx = np.argsort(sim_scores)[-k:]
            sim_scores = sim_scores[idx]
            ratings = ratings[idx]
        return np.dot(sim_scores, ratings) / np.sum(sim_scores)

    # 对于每个用户，推荐前k个未点击过的物品
    def recommend(user_id, R, sim_matrix, k=3):
        n = R.shape[1]
        # 对于每个未点击过的物品，计算预测评分，并按照预测评分排序，推荐前k个未点击过的物品
        scores = np.zeros(n)
        for i in range(n):
            if R[user_id, i] == 0:
                scores[i] = user_id.predict_rating(user_id, i, R, sim_matrix)
        idx = np.argsort(scores)[::-1][:k]
        return idx

    def Get_hits_list(self, ctx):
        query = dict(ctx.query)
        service = self.service
        if "user_id" in query:
            user_id = query.pop("user_id")
            if user_id == '':
                return self.Get_list(ctx)
            hitsCountSql = "SELECT COUNT( hits_id ) AS hits_count, source_id FROM hits WHERE source_table = 'hot_books' AND user_id = "+user_id+" GROUP BY source_id"
            maxHitsCountSql = "SELECT t1.source_id FROM ( "+hitsCountSql+" ) t1 ORDER BY hits_count DESC LIMIT 0,1"
            typeSql = "SELECT commodity_category FROM hot_books WHERE hot_books_id = ( "+maxHitsCountSql+" )"
            productListSql = "SELECT * FROM hot_books WHERE commodity_category = ( "+typeSql+" )"
            sql = productListSql + " ORDER BY hits DESC LIMIT 0,4"
            data = service.run(sql)
            return {"result": {"list": data, "count": len(data)}}
        return self.Get_list(ctx)

