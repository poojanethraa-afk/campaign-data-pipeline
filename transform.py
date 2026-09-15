from pyspark.sql  import SparkSession
from pyspark.sql.functions import col

session= SparkSession.builder.appName("CampaignTransform").getOrCreate()

def transform_data(pandas_df):
    spark_df= session.createDataFrame(pandas_df)
    spark_df =     spark_df.withColumn("TotalSpend", col("MntWines") + col("MntFruits") + col("MntMeatProducts") + col("MntFishProducts") + col("MntSweetProducts") + col("MntGoldProds"))
    spark_df = spark_df.withColumn("TotalCampaignsAccepted", col("AcceptedCmp1") + col("AcceptedCmp2") + col("AcceptedCmp3") + col("AcceptedCmp4") + col("AcceptedCmp5"))
    return spark_df

def get_campaign_performance_by_segment(spark_df):
     performance = spark_df.groupby("Education").avg("TotalCampaignsAccepted")
     return performance

if __name__ == "__main__":
         from extract import extract_data
         pandas_df = extract_data()
         transformed_df = transform_data(pandas_df)
         transformed_df.show(5)
         performance = get_campaign_performance_by_segment(transformed_df)
         performance.show()