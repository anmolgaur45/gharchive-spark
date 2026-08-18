from pyspark.sql import SparkSession


def main():

    spark = SparkSession.builder.appName("Verify spark env").master("local[*]").getOrCreate()

    print(spark.version)

    spark.range(5).show()
    print('Spark environment ok')

    spark.stop()


if __name__ == "__main__":
    main()