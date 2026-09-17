from pyspark.sql  import SparkSession
from pyspark.sql.functions import col

session= SparkSession.builder.appName("CampaignTransform").getOrCreate()

def transform_data(pandas_df):
    spark_df= session.createDataFrame(pandas_df)
    spark_df =         spark_df = spark_df.withColumn("MonthlyPayment", col("Credit amount") / col("Duration"))
    return spark_df

def get_credit_profile_by_purpose(spark_df):
     performance = spark_df.groupby("Purpose").avg("Credit amount")
     return performance

if __name__ == "__main__":
         from extract import extract_data
         pandas_df = extract_data()
         transformed_df = transform_data(pandas_df)
         transformed_df.show(5)
         performance = get_credit_profile_by_purpose(transformed_df)
         performance.show()