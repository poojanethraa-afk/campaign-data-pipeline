from extract import extract_data
from quality_checks import run_quality_checks
from transform import transform_data, get_campaign_performance_by_segment
from load import load_data

def run_pipeline():
    print("STEP 1: Extract")
    raw_df = extract_data()
    print("STEP 2: Quality Checks")
    passed = run_quality_checks(raw_df)
    if not passed:
        print("WARNING: Quality checks failed — continuing anyway (see details above)")
    print("STEP 3: Transform")
    transformed_df = transform_data(raw_df)
    print("STEP 4: Load")
    load_data(transformed_df, "customers")
    performance_df = get_campaign_performance_by_segment(transformed_df)
    load_data(performance_df, "campaign_performance_by_education")

if __name__ == "__main__":
    run_pipeline()