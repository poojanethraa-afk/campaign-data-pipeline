import pandas as pd
from quality_checks import check_missing_values, check_duplicates, check_credit_amount_range

def test_check_missing_values_passes_with_no_nulls():
    df = pd.DataFrame({'Income': [50000, 60000, 70000]})
    assert check_missing_values(df) == True

def test_check_missing_values_fails_with_nulls():
    df = pd.DataFrame({"Income": [50000, None, 70000]})
    assert check_missing_values(df) == False

def test_check_duplicates_passes_with_unique_ids():
    df = pd.DataFrame({'Age': [25, 30, 45]})
    assert check_duplicates(df) == True

def test_check_duplicates_fails_with_duplicate_ids():
    df = pd.DataFrame({'Age': [25, 25, 45]})
    assert check_duplicates(df) == False

def test_check_credit_amount_range_passes_with_valid_amount():
    df = pd.DataFrame({"Credit amount": [5000, 6000]})
    assert check_credit_amount_range(df) == True

def test_check_credit_amount_range_fails_with_negative_amount():
    df = pd.DataFrame({"Credit amount": [-100, 6000]})
    assert check_credit_amount_range(df) == False