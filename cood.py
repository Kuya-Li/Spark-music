import datetime

from pyspark.sql import Row
from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col
sql = "INSERT INTO `access_token` (`token`,`user_id`) VALUES ('79e919c8daf227b68abd082207593143','1');"
# sql ="SELECT * FROM(SELECT *, ROW_NUMBER() OVER( ORDER BY article_id) as row_num FROM article) tmp WHERE row_num BETWEEN 1 AND 10"
up = {'ad_id': 4, 'title': '更高123123', 'content': '<p>222</p>', 'url': '11', 'img': '', 'display': 0, 'hits': 0, 'location': '顶部广告'}

current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
spark = SparkSession \
    .builder \
    .appName("SparkByExamples.com") \
    .config("spark.sql.warehouse.dir", "/hive/warehouse/dir") \
    .config("hive.metastore.uris", "thrift://127.0.0.1:9083") \
    .enableHiveSupport() \
    .getOrCreate()
try:
    # 先查询hive中的表数据
    existing_df = spark.sql(f"SELECT * FROM ad ")
    # num_rows = existing_df.count()
    # 更新表主键ID
    up[f'ad_id'] = 114
    up['create_time'] = current_timestamp
    up['update_time'] = current_timestamp
    # 将数据进行排序
    sorted_data = {k: up[k] for k in sorted(up)}
    new_row = Row(**sorted_data)
    # 创建一个pyspark的DataFrame数据集合
    new_df = spark.createDataFrame([new_row], schema=existing_df.schema)
    # append ,追加保存
    new_df.write.mode('append').insertInto('ad')
except Exception as e:
    print(e.args)
    spark.stop()
spark.stop()