import pandas as pd
import re

def load_csv(filepath):
    """Loads a CSV file and raises errors for missing or empty files."""
    try:
        df = pd.read_csv(filepath)
        if df.empty:
            raise ValueError("File is empty")
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    except pd.errors.EmptyDataError:
        # Pandas throws this before it even creates the dataframe if the file is totally blank
        raise ValueError("File is empty")

def clean_phone(phone):
    """Removes non-numeric characters from a phone number string."""
    if pd.isna(phone) or not isinstance(phone, str):
        return None
    cleaned = re.sub(r'\D', '', phone)
    return cleaned if cleaned else None

def validate_email(email):
    """Validates an email address against a standard regex pattern."""
    if pd.isna(email) or not isinstance(email, str):
        return False
    regex = r"^[^@]+@[^@]+\.[a-zA-Z0-9.-]+$"
    return bool(re.match(regex, email))