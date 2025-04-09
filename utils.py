# -*- coding: utf-8 -*-
from datetime import datetime

from pyhive.exc import OperationalError
from pyspark.sql import SparkSession

from SqoopImport import Sqoop
from pyhive.hive import Connection as hive_connect
from pymysql import connect as mysql_connect


class HiveToMysql:
    def __init__(self, database, mysql_host=None, port=None):
        # self.mysql_host = '127.0.0.1'
        # self.mysql_port = 4306
        # self.mysql_host =
        if mysql_host:
            self.mysql_host = mysql_host
        else:
            self.mysql_host = '172.19.0.5'
        if port:
            self.mysql_port = port
        else:
            self.mysql_port = 3306

        self.mysql_coon = mysql_connect(host=self.mysql_host, port=self.mysql_port
                                        , user='root', password='123456',
                                        database=database)
        self.hive_coon = hive_connect(host='127.0.0.1', port=10000, database='default')
        self.hive_cur = self.hive_coon.cursor()
        self.mysql_cur = self.mysql_coon.cursor()
        self.table_filed_dict = dict()
        self.table_filed_primary = dict()
        self.mysql_tables_list = []
        self.init_mysql_database()
        self.init_mysql_database_field()
        self.sqoop = Sqoop(
            fs="hdfs://localhost:9000",
            connect=f"jdbc:mysql://{self.mysql_host}:{self.mysql_port}/{database}",
            username="root",
            password="123456",
            hive_import=True,
            direct=True,
            # hive_overwrite=True,
            # create_hive_table=True,
            fields_terminated_by="','",
            m=1,
        )
        self.debug = True

    def init_mysql_database(self):
        self.mysql_cur.execute('show tables')
        resp = self.mysql_cur.fetchall()
        for i in resp:
            # print(i)
            self.mysql_tables_list.append(i[0])
            key_filed_sql = f"show index from `{i[0]}` where Key_name='PRIMARY'"
            self.mysql_cur.execute(key_filed_sql)
            key_resp = self.mysql_cur.fetchall()
            self.table_filed_primary[i[0]] = key_resp[0][4]


    def init_mysql_database_field(self):
        """
        初始化mysql字段
        :return:
        """
        for i in self.mysql_tables_list:
            show_sql = f"DESCRIBE `{i}`"
            self.mysql_cur.execute(show_sql)
            describe = self.mysql_cur.fetchall()
            self._get_table_field_data(describe, i)

    def _hive_columns_check(self, column):
        """
        检查字段
        :return:
        """
        map_dict = {'int unsigned': 'bigint',
                    'int': 'int',
                    'mediumint unsigned': 'int',
                    'double': 'DOUBLE',
                    'smallint unsigned': 'SMALLINT',
                    'varchar': 'STRING',
                    'timestamp': 'TIMESTAMP',
                    'text': 'STRING',
                    'longtext': 'STRING',
                    'date': 'DATE',
                    'mediumint': 'INT',
                    'datetime': 'STRING'}
        if 'varchar' in column:
            return 'STRING'
        if 'tinyint' in column:
            return 'TINYINT'
        if 'double' in column:
            return 'DOUBLE'
        return map_dict[column]

    def init_hive_table(self):
        """
        初始化hive数据库
        :return:
        """
        for i in self.mysql_tables_list:

            get_table_field_len = len(self.table_filed_dict[i].keys())
            hive_create = f"CREATE TABLE IF NOT EXISTS `{i}` ("
            # 外部表
            fileds = self.table_filed_dict[i]
            sorted_data = {k: fileds[k] for k in sorted(fileds)}
            hive_external_create = f"CREATE EXTERNAL TABLE IF NOT EXISTS `EXTERNAL_{i}` ("
            for index, field in enumerate(sorted_data):
                rate = f"`{field}` {self._hive_columns_check(self.table_filed_dict[i][field])}"
                if index + 1 == get_table_field_len:
                    hive_create += rate + ") STORED AS ORC TBLPROPERTIES ('transactional'='true')"

                    hive_external_create += rate + ") ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE "
                else:
                    hive_create += rate + ","
                    hive_external_create += rate + ","
            print(f"创建本地表{i}")
            self.hive_cur.execute(hive_create)
            print(f"创建外部表{i}")
            self.hive_cur.execute(hive_external_create)

    def init_hive_data(self):
        """sync hive database"""
        for table in self.mysql_tables_list:
            self.hive_cur.execute(f"DROP TABLE IF EXISTS `{table}`")
            fileds = self.table_filed_dict[table]
            sorted_data = {k: fileds[k] for k in sorted(fileds)}
            filed = []

            for i in sorted_data.keys():
                filed.append(f'`{i}`')
            _ = ','.join(filed)
            sql = f"select {_} from `{table}` WHERE $CONDITIONS"
            self.sqoop.set_param('--hive-table', table)
            self.sqoop.set_param('--target-dir', f"/home/hive/{table}")
            self.sqoop.set_param('--query', f"'{sql}'")
            self.sqoop.set_param('--split-by', f"'{self.table_filed_primary[table]}'")
            # self.sqoop.set_param('--direct', '')
            cmd = self.sqoop.command()
            cmd = cmd.replace('None ', '', 1)
            print(cmd)
            response = self.sqoop.perform_import(cmd)
            if response.returncode == 0:
                print(f"{table} 数据备份hadoop成功")
                print(f"{table} 数据同步中")
                self.hive_cur.execute(f'INSERT OVERWRITE TABLE `{table}`  SELECT * FROM `{table}`')
            else:
                print(cmd)
                print(response.stderr)

    # def sync_hive_data(self):
    #     for table in self.mysql_tables_list:

    def init_mysql_to_hive(self):
        # spark = SparkSession \
        #     .builder \
        #     .appName("SparkByExamples.com") \
        #     .config("spark.sql.warehouse.dir", "/hive/warehouse/dir") \
        #     .config("hive.metastore.uris", "thrift://127.0.0.1:9083") \
        #     .enableHiveSupport() \
        #     .getOrCreate()
        for i in self.mysql_tables_list:
            fileds = self.table_filed_dict[i]
            sorted_data = list({k: fileds[k] for k in sorted(fileds)})
            sql = "select " + ','.join([f'`{field}`' for field in sorted_data]) + f' from `{i}`'
            # print(sql)
            self.mysql_cur.execute(sql)
            result = self.mysql_cur.fetchall()
            columns = [desc[0] for desc in self.mysql_cur.description]  # 获取查询结果的字段名
            result_value = []
            # result_dict = []
            # for row in result:
            #     row_dict = {}
            #     for column in range(len(columns)):
            #         if type(row[column]) == datetime:
            #             date_value = row[column]
            #             # date_value.stript
            #             row_dict[columns[column]] = date_value.strftime('%Y-%m-%d %H:%m:%S')
            #         else:
            #             row_dict[columns[column]] = row[column]
            #     result_dict.append(row_dict)
            for row in result:
                row_dict = []
                for column in range(len(columns)):
                    if type(row[column]) == datetime:
                        date_value = row[column]
                        # date_value.stript
                        row_dict.append(date_value.strftime('%Y-%m-%d %H:%m:%S'))
                    else:
                        row_dict.append(row[column])
                result_value.append(tuple(row_dict))
            try:

                # for rowv in row.keys():
                #     print(type(rowv))
                # filed = list(row.keys())
                # insert_query  = f'INSERT INTO `{i}` (' + ','.join([f'`{rowv}`' for rowv in row.keys()]) + ") values " + f'''({','.join([str(row[rowv]) if type(row[rowv]) == int else f"'{str(row[rowv])}'" for rowv in row.keys()])})'''
                m = ','.join(['%s' for s in range(len(result))])
                insert_query = f'INSERT INTO `{i}` (' + ','.join(
                    [f'`{field}`' for field in sorted_data]) + ") values (" + m + ")"
                print(insert_query)
                print(result_value)
                self.hive_cur.executemany(insert_query, result_value)
                # self.hive_cur.commit()
            except Exception as e:
                print(e.args)

    def _get_table_field_data(self, table_data, name):
        map_filed_type = dict()
        for table in table_data:
            map_filed_type[table[0]] = table[1]
        self.table_filed_dict[name] = map_filed_type

    def test(self):
        self.hive_cur.execute(
            "load data inpath '/user/hive/warehouse/test.csv' OVERWRITE into table EXTERNAL_access_token")
        # hive临时表到目标表
        table = 'access_token'
        self.hive_cur.execute(f'INSERT OVERWRITE TABLE `{table}`  SELECT * FROM `EXTERNAL_{table}`')


# dataclass = HiveToMysql('CS866740_20220728155643', '127.0.0.1', 4306)
if __name__ == '__main__':
    dataclass = HiveToMysql('CS866740_20220728155643')
    dataclass.init_hive_table()
    # # dataclass.test()
    # dataclass.init_hive_table()
    dataclass.init_hive_data()
    # dataclass.init_mysql_to_hive()
