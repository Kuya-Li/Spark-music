

import org.apache.spark.sql.*;
import org.apache.spark.sql.functions;
import java.util.Map;
import java.util.HashMap;
import java.util.Date;
import java.util.ArrayList;
import java.text.SimpleDateFormat;


public class Utils {

    public static void main(String[] args) {
        Map<String, Object> map1 = new HashMap<>();
        map1.put("key1", "value1");
        map1.put("key2", "value2");

        Map<String, Object> map2 = new HashMap<>();
        map2.put("key2", "updatedValue2");
        map2.put("key3", "value3");

        Map<String, Object> result = objUpdate(map1, map2);
        System.out.println(result);  // 输出: {key1=value1, key2=updatedValue2, key3=value3}
    }

    public static Map<String, Object> objUpdate(Map<String, Object>... configs) {
        Map<String, Object> mergedConfig = new HashMap<>();
        for (Map<String, Object> config : configs) {
            mergedConfig.putAll(config);
        }
        return mergedConfig;
    }
}

public class SqlQueryBuilder {
    public static void main(String[] args) {
        Map<String, Object> queryDict = new HashMap<>();
        // 示例查询条件
        queryDict.put("name", "Alice");
        queryDict.put("age_min", 25);
        queryDict.put("age_max", 30);

        String whereClause = toWhere(queryDict, true);
        System.out.println(whereClause);
    }

    public static String toWhere(Map<String, Object> queryDict, boolean like) {
        String where = "";
        for (Map.Entry<String, Object> entry : queryDict.entrySet()) {
            String key = entry.getKey();
            Object val = entry.getValue();

            if (key.endsWith("_min")) {
                where += " AND `" + key.replace("_min", "") + "` >= " + escape(val.toString());
            } else if (key.endsWith("_max")) {
                where += " AND `" + key.replace("_max", "") + "` <= " + escape(val.toString());
            } else if (val instanceof String) {
                if (like) {
                    where += " AND `" + key + "` LIKE '%" + escape(val.toString()) + "%'";
                } else {
                    where += " AND `" + key + "` = '" + escape(val.toString()) + "'";
                }
            } else {
                where += " AND `" + key + "` = " + val;
            }
        }
        return where.length() > 0 ? where.replaceFirst(" AND ", "") : where;
    }

    // 这个方法用于转义 SQL 查询中的特殊字符，防止 SQL 注入
    // 根据实际情况进行实现
    private static String escape(String value) {
        return value.replace("'", "''");
    }
}

"""
更新
这段代码的主要功能是从一个 Hive 表中读取数据，
然后根据传入的 body 字典中的信息更新表中的数据，
最后将更新后的数据写回 Hive 表。
"""
public class UpdateTable {
    public static void main(String[] args) {
        // 创建 SparkSession
        SparkSession spark = SparkSession
                .builder()
                .appName("SparkByExamples.com")
                .config("spark.sql.warehouse.dir", "/hive/warehouse/dir")
                .config("hive.metastore.uris", "thrift://127.0.0.1:9083")
                .enableHiveSupport()
                .getOrCreate();

        try {
            // 获取配置和数据
            Map<String, String> config = Utils.objUpdate(self.config, config);
            String table = config.get("table");
            Map<String, String> body = new HashMap<>();
            Map<String, String> query = new HashMap<>();

            // 从 Hive 表中读取数据
            Dataset<Row> df = spark.sql("SELECT * FROM " + table);

            // 更新 DataFrame 中的数据
            for (String key : body.keySet()) {
                df = df.withColumn(key, functions.when(functions.col(table + "_id").equalTo(query.get(table + "_id")), body.get(key)).otherwise(functions.col(key)));
            }

            // 获取当前时间戳
            String currentTimestamp = new java.text.SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(new java.util.Date());

            // 更新 update_time 列
            Dataset<Row> newDf = df.withColumn("update_time", functions.when(functions.col(table + "_id").equalTo(query.get(table + "_id")), currentTimestamp).otherwise(functions.col("update_time")));

            // 创建临时视图
            newDf.createOrReplaceTempView("temp_" + table);

            // 使用 SQL 语句将临时视图的数据写回 Hive 表
            spark.sql("INSERT OVERWRITE TABLE default." + table + " SELECT * FROM temp_" + table);
        } catch (Exception e) {
            // 打印错误信息
            e.printStackTrace();
            // 停止 SparkSession
            spark.stop();
        }

        // 停止 SparkSession
        spark.stop();
    }
}

"""
查询
从配置中获取表名和查询条件。
根据这些信息构建 SQL 语句。
执行 SQL 语句，并将结果转换为一个字典列表。
打印结果。
"""

public class ExecuteSql {
    public static void main(String[] args) {
        // 创建 SparkSession
        SparkSession spark = SparkSession
                .builder()
                .appName("SparkByExamples.com")
                .config("spark.sql.warehouse.dir", "/hive/warehouse/dir")
                .config("hive.metastore.uris", "thrift://127.0.0.1:9083")
                .enableHiveSupport()
                .getOrCreate();

        try {
            // 获取配置和数据
            Map<String, String> config = Utils.objUpdate(self.config, config);
            Map<String, String> query = new HashMap<>();

            // 构建 SQL 语句
            String sql = toGetSql(query, config);

            // 执行 SQL 语句，并将结果转换为字典
            Dataset<Row> sparkDF = spark.sql(sql);
            List<Map<String, Object>> result = sparkDF.collectAsList().stream().map(row -> {
                Map<String, Object> rowMap = new HashMap<>();
                for (int i = 0; i < row.size(); i++) {
                    rowMap.put(row.schema().fields()[i].name(), row.get(i));
                }
                return rowMap;
            }).collect(Collectors.toList());

            // 打印结果
            System.out.println("-------------spark on hive 响应结果");
            System.out.println(result);
        } catch (Exception e) {
            // 打印错误信息
            e.printStackTrace();
            // 停止 SparkSession
            spark.stop();
        }

        // 停止 SparkSession
        spark.stop();
    }

    public static String toGetSql(Map<String, String> query, Map<String, String> config) {
        // ...
        return sql;
    }
}
"""
插入
从配置中获取表名。
从 Hive 表中获取行数。
创建一个新的数据行，其中包括一个新的 ID（基于行数）、创建时间和更新时间。
将新的数据行插入到 Hive 表中。
"""
public class InsertIntoTable {
    public static void main(String[] args) {
        // 创建 SparkSession
        SparkSession spark = SparkSession
                .builder()
                .appName("SparkByExamples.com")
                .config("spark.sql.warehouse.dir", "/hive/warehouse/dir")
                .config("hive.metastore.uris", "thrift://127.0.0.1:9083")
                .enableHiveSupport()
                .getOrCreate();

        try {
            // 获取配置和数据
            Map<String, String> config = Utils.objUpdate(self.config, config);
            String table = config.get("table");
            Map<String, String> body = new HashMap<>();
            Map<String, String> newBody = new HashMap<>(body);

            // 获取表中的行数
            Dataset<Row> countDf = spark.sql("SELECT COUNT(*) FROM " + table);
            long count = countDf.collectAsList().get(0).getLong(0);

            // 获取当前时间戳
            String currentTimestamp = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(new Date());

            // 更新 newBody
            newBody.put(table + "_id", String.valueOf(count + 1));
            newBody.put("create_time", currentTimestamp);
            newBody.put("update_time", currentTimestamp);

            // 从 Hive 表中读取数据
            Dataset<Row> existingDf = spark.sql("SELECT * FROM " + table);

            // 创建新的 DataFrame
            List<Row> newRowList = new ArrayList<>();
            newRowList.add(RowFactory.create(newBody.values().toArray()));
            Dataset<Row> newDf = spark.createDataFrame(newRowList, existingDf.schema());

            // 将新的数据行插入到 Hive 表中
            newDf.write().mode(SaveMode.Append).insertInto(table);
        } catch (Exception e) {
            // 打印错误信息
            e.printStackTrace();
            // 停止 SparkSession
            spark.stop();
        }

        // 停止 SparkSession
        spark.stop();
    }
}
"""
删除
从配置中获取表名和查询条件。
构建一个 WHERE 子句，用于过滤掉需要删除的数据。
从 Hive 表中读取数据，应用 WHERE 子句进行过滤。
将过滤后的数据写回到同一个 Hive 表中
"""

public class FilterAndOverwriteTable {
    public static void main(String[] args) {
        // 创建 SparkSession
        SparkSession spark = SparkSession
                .builder()
                .appName("SparkByExamples.com")
                .config("spark.sql.warehouse.dir", "/hive/warehouse/dir")
                .config("hive.metastore.uris", "thrift://127.0.0.1:9083")
                .enableHiveSupport()
                .getOrCreate();

        try {
            // 获取配置和数据
            Map<String, String> config = Utils.objUpdate(self.config, config);
            String table = config.get("table");
            Map<String, String> query = new HashMap<>();

            // 构建 WHERE 子句
            String where = "";
            for (Map.Entry<String, String> entry : query.entrySet()) {
                where += entry.getKey() + " != " + entry.getValue() + " AND ";
            }
            // 移除最后的 " AND "
            if (!where.isEmpty()) {
                where = where.substring(0, where.length() - 5);
            }

            // 从 Hive 表中读取数据
            Dataset<Row> existingDf = spark.sql("SELECT * FROM " + table + " WHERE " + where);

            // 将过滤后的数据写回 Hive 表
            existingDf.write().mode(SaveMode.Overwrite).insertInto(table);
        } catch (Exception e) {
            // 打印错误信息
            e.printStackTrace();
            // 停止 SparkSession
            spark.stop();
        }

        // 停止 SparkSession
        spark.stop();
    }
}



import java.sql.SQLException;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;
import java.sql.DriverManager;
import java.sql.Connection;

"""
java使用hive--------------------------------------------------------
"""
public class HiveJdbcClient {
    private static String driverName = "org.apache.hive.jdbc.HiveDriver";

    public static void main(String[] args) throws SQLException {
        try {
            Class.forName(driverName);
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
            System.exit(1);
        }

        // 创建连接
        Connection con = DriverManager.getConnection("jdbc:hive2://localhost:10000/default", "", "");

        // 创建声明
        Statement stmt = con.createStatement();

        // 执行 SQL 查询
        String sql = "SELECT * FROM mytable";
        System.out.println("Running: " + sql);
        ResultSet res = stmt.executeQuery(sql);
        while (res.next()) {
            System.out.println(String.valueOf(res.getInt(1)) + "\t" + res.getString(2));
        }
        // 关闭连接
        con.close();
    }
}
"""
hive连接
"""
public class HiveConnection {
    private static String driverName = "org.apache.hive.jdbc.HiveDriver";

    public static Connection getConnection() {
        try {
            Class.forName(driverName);
            Connection con = DriverManager.getConnection("jdbc:hive2://127.0.0.1:10000/default", "账户", "密码");
            return con;
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
}
"""
hive插入

"""
public class HiveInsert {
    public static void main(String[] args) {
        try {
            Connection con = HiveConnection.getConnection();
            Statement stmt = con.createStatement();
            String sql = "INSERT INTO mytable (id, name) VALUES (1, 'Alice')";
            stmt.execute(sql);
            con.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
"""
hive更新
"""
public class HiveUpdate {
    public static void main(String[] args) {
        try {
            Connection con = HiveConnection.getConnection();
            Statement stmt = con.createStatement();
            stmt.execute("SET hive.txn.manager=org.apache.hadoop.hive.ql.lockmgr.DbTxnManager");
            stmt.execute("SET hive.support.concurrency=true");
            stmt.execute("SET hive.enforce.bucketing=true");
            stmt.execute("SET hive.exec.dynamic.partition.mode=nonstrict");
            stmt.execute("SET hive.compactor.initiator.on=true");
            stmt.execute("SET hive.compactor.worker.threads=1");

            String sql = "UPDATE mytable SET name='Bob' WHERE id=1";
            stmt.execute(sql);

            con.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
"""
hive删除
"""
public class HiveDelete {
    public static void main(String[] args) {
        try {
            Connection con = HiveConnection.getConnection();
            Statement stmt = con.createStatement();
            stmt.execute("SET hive.txn.manager=org.apache.hadoop.hive.ql.lockmgr.DbTxnManager");
            stmt.execute("SET hive.support.concurrency=true");
            stmt.execute("SET hive.enforce.bucketing=true");
            stmt.execute("SET hive.exec.dynamic.partition.mode=nonstrict");
            stmt.execute("SET hive.compactor.initiator.on=true");
            stmt.execute("SET hive.compactor.worker.threads=1");

            String sql = "DELETE FROM mytable WHERE id=1";
            stmt.execute(sql);

            con.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}