from pyspark.sql.functions import to_json, struct, lit

alerts = (
    df
    .filter(col("amount") > 3000)
    .select(
        to_json(
            struct(
                "tx_id", "user_id", "amount", "store", "category",
                col("timestamp").cast("string"),
                lit("HIGH").alias("alert_level"),
            )
        ).alias("value")    # Kafka wymaga kolumny 'value'
    )
)

alert_query = (
    alerts.writeStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "broker:9092")
    .option("topic", "alerts")
    .outputMode("append")
    .start()
)
print("Strumień alertów uruchomiony. Zatrzymaj ręcznie: alert_query.stop()")
