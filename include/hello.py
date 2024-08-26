# hello_world.py
from pyspark.sql import SparkSession


def main():
    # Initialize Spark Session
    spark = SparkSession.builder.appName("InitArrayPrintExample").getOrCreate()

    # Create an array with 1000 elements
    array = list(range(1, 1001))

    # Parallelize the array into an RDD
    rdd = spark.sparkContext.parallelize(
        array, numSlices=4
    )  # numSlices specifies the number of partitions

    # Print each element to the console
    rdd.foreach(lambda x: print(x))

    # Stop Spark session
    spark.stop()


if __name__ == "__main__":
    main()
