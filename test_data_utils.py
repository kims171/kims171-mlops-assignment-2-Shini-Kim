import pytest
import pandas as pd
from data_utils import load_csv, clean_phone, validate_email

# ==========================================
# Tests for load_csv
# ==========================================
def test_load_csv_success(tmp_path):
    # tmp_path is a built-in pytest fixture for creating temporary files
    test_file = tmp_path / "test_data.csv"
    test_file.write_text("col1,col2\n1,2")
    
    df = load_csv(str(test_file))
    assert not df.empty
    assert list(df.columns) == ['col1', 'col2']
    assert len(df) == 1

def test_load_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_csv("non_existent_file.csv")

def test_load_csv_empty_file(tmp_path):
    empty_file = tmp_path / "empty.csv"
    empty_file.write_text("")
    with pytest.raises(ValueError, match="File is empty"):
        load_csv(str(empty_file))

# ==========================================
# Tests for clean_phone
# ==========================================
def test_clean_phone_various_formats():
    assert clean_phone("(910) 600-2089") == "9106002089"
    assert clean_phone("928 552 7966") == "9285527966"
    assert clean_phone("486.684.7394") == "4866847394"
    assert clean_phone("562-464-9551") == "5624649551"

def test_clean_phone_invalid_inputs():
    assert clean_phone("no_numbers_here") is None
    assert clean_phone(None) is None
    assert clean_phone(float('nan')) is None # Handles pandas NaN

# ==========================================
# Tests for validate_email
# ==========================================
def test_validate_email_valid():
    assert validate_email("user4875@example.com") is True
    assert validate_email("user.name+tag@sub.domain.co.uk") is True

def test_validate_email_invalid():
    assert validate_email("plainaddress") is False
    assert validate_email("@domain.com") is False
    assert validate_email("user@no_dot_com") is False

def test_validate_email_edge_cases():
    assert validate_email("") is False
    assert validate_email(None) is False
    assert validate_email(float('nan')) is False