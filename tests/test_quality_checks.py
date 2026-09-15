import pandas as pd
from quality_checks import check_missing_values, check_duplicates, check_income_range

def test_check_missing_values_passes_with_no_nulls():
    df = pd.DataFrame({'Income': [50000, 60000, 70000]})
    assert check_missing_values(df) == True

def test_check_missing_values_fails_with_nulls():
        df = pd.DataFrame({"Income": [50000, None, 70000]})
        assert check_missing_values(df) == False

def test_check_duplicates_passes_with_unique_ids():
      df= pd.DataFrame({'ID':[1,2,3]})
      assert check_duplicates(df) == True

def test_check_duplicates_fails_with_duplicate_ids():
      df= pd.DataFrame({'ID':[1,1,3]})
      assert check_duplicates(df) == False

def test_check_income_range_passes_with_valid_income():
        df = pd.DataFrame({"Income": [50000, 60000]})
        assert check_income_range(df) == True

def test_check_income_range_fails_with_negative_income():
        df = pd.DataFrame({"Income": [-100, 60000]})
        assert check_income_range(df) == False
