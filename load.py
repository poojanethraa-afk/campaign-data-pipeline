from pathlib import Path
from sqlalchemy import create_engine
DB_PATH = f"sqlite:///{Path(__file__).resolve().parent / 'data' / 'campaign_data.db'}"

def load_data(spark_df, table_name):
    engine= create_engine(DB_PATH)
    pandas_df = spark_df.toPandas()
    pandas_df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f"Loaded {len(pandas_df)} rows into '{table_name}' table")

if __name__ == "__main__":
    from extract import extract_data
    from transform import transform_data, get_credit_profile_by_purpose
    raw_df = extract_data()
    transformed_df = transform_data(raw_df)
    load_data(transformed_df, "customers")
    performance_df = get_credit_profile_by_purpose(transformed_df)
    load_data(performance_df, "credit_profile_by_purpose")



