import pandas as pd
def check_missing_values(df: pd.DataFrame) -> bool:
    missing = df.isnull().sum()
    missing = missing[missing > 0]
    if len(missing) > 0:
        print(f"FAIL: missing values found in columns:\n{missing}")
        return False
    print("PASS: No missing values found.")
    return True


def check_duplicates(df: pd.DataFrame) -> bool:
    duplicate_count = df.duplicated().sum()
    if duplicate_count > 0:
        print(f"FAIL: {duplicate_count} duplicate rows found")
        return False
    print("PASS: No duplicate rows found.")
    return True

def  check_credit_amount_range(df:pd.DataFrame) -> bool:
    invalid= df[(df['Credit amount'] < 0) | (df['Credit amount'] > 20000)]
    if len(invalid) > 0:
        print(f"FAIL: {len(invalid)} rows with invalid credit amount range found")
        return False
    print("PASS: All values are within the valid range.")
    return True
def run_quality_checks(df: pd.DataFrame) -> bool:
    results = [
        check_missing_values(df),
        check_duplicates(df),
        check_credit_amount_range(df), ]

    return all(results)

if __name__ == "__main__":
    from extract import extract_data
    df = extract_data()
    passed = run_quality_checks(df)
    if passed:
        print("All quality checks passed.")
    else:
        print("Some quality checks failed.")