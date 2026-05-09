from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, to_timestamp, window, count, sum as _sum, round as _round
from pyspark.sql.types import StructType, StructField, StringType, DoubleType
 
tx_schema = StructType([
    StructField("tx_id",     StringType()),
    StructField("user_id",   StringType()),
    StructField("amount",    DoubleType()),
    StructField("store",     StringType()),
    StructField("category",  StringType()),
    StructField("timestamp", StringType()),
])
 
 
spark = (
    SparkSession.builder
    .appName("Lab4-Kafka")
    .getOrCreate()
)
spark.sparkContext.setLogLevel("WARN")
 
kafka_raw = (spark.readStream.format("kafka").option("kafka.bootstrap.servers", "broker:9092").option("subscribe", "transactions")
.load())
 
parsed = kafka_raw.select(
    from_json(col("value").cast("string"), tx_schema).alias("tx")
).select("tx.*").withColumn("timestamp", to_timestamp("timestamp"))

group = (
    parsed
    .withWatermark("timestamp", "3 seconds")
    .groupBy(window("timestamp", "10 seconds"), "category")
    .agg(
        count("tx_id").alias("liczba_tx"),
        _round(_sum("amount"), 2).alias("suma_PLN"),
    )
)


q = (group.writeStream.format("console") 
    .outputMode("complete") .option("truncate", False)
    .start())
 
q.awaitTermination()
