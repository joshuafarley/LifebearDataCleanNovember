import pandas as pd
import re

# File paths for input, output, and garbage files
input_file = '/content/3.6M-Japan-lifebear.com-Largest-Notebook-App-UsersDB-csv-2019.csv'
output_file = 'cleaned_lifebear_8.csv'
garbage_file = 'RemovedRecords_8.csv'

def extract(input_file):
    try:
        # Read the CSV file with UTF-8 encoding (or adjust if needed)
       df = pd.read_csv(input_file, delimiter=';', encoding='utf-8')
       return df
    except Exception as e:
        print(f"Error reading input file: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error

def transform(df):
    if df.empty:
        print("DataFrame is empty. Transformation cannot proceed.")
        return df, pd.DataFrame()

    # Check if the 'login_id' column exists in the DataFrame
    if 'login_id' not in df.columns:
        print("'login_id' column is missing in the dataset.")
        return df, pd.DataFrame()

    # Initialize invalid rows dataframe with an "Issue" column
    invalid_rows = pd.DataFrame()

    # Clean invalid characters
    def clean_text(text):
        if isinstance(text, str):
            return re.sub(r'â€|[^\x00-\x7F]+', '', text)  # Removes non-ASCII characters
        return text

    # Validate email format
    def validate_email(email):
        if isinstance(email, str):
            if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):  # Simple regex for email validation
                return email
            else:
                return None
        return email

    # Apply cleaning functions
    df_clean = df.copy()

    # Step 1: Clean text for all columns
    for column in df_clean.columns:
        df_clean[column] = df_clean[column].map(clean_text)

    # Step 2: Validate and clean email addresses
    if 'mail_address' in df_clean.columns:
        df_clean['mail_address'] = df_clean['mail_address'].map(validate_email)
        invalid_email_rows = df_clean[df_clean['mail_address'].isnull()].copy()
        if not invalid_email_rows.empty:
            invalid_email_rows['Issue'] = 'Invalid mail_address'
            invalid_rows = pd.concat([invalid_rows, invalid_email_rows], ignore_index=True)

    # Step 3: Remove time from 'created_at' column, keeping only the date
    if 'created_at' in df_clean.columns:
        df_clean['created_at'] = pd.to_datetime(df_clean['created_at'], errors='coerce').dt.date

    # Step 4: Identify and handle rows where both login_id and mail_address are null or empty
    invalid_login_mail_rows = df_clean[(df_clean['login_id'].isnull() | (df_clean['login_id'] == '')) &
                                       (df_clean['mail_address'].isnull() | (df_clean['mail_address'] == ''))].copy()
    if not invalid_login_mail_rows.empty:
        invalid_login_mail_rows['Issue'] = 'Both login_id and mail_address blank'
        invalid_rows = pd.concat([invalid_rows, invalid_login_mail_rows], ignore_index=True)

    # Remove rows where both login_id and mail_address are null or empty
    df_clean = df_clean[~((df_clean['login_id'].isnull() | (df_clean['login_id'] == '')) &
                          (df_clean['mail_address'].isnull() | (df_clean['mail_address'] == '')))]

    # Step 5: Handle duplicate mail_address (if the column exists)
    if 'mail_address' in df_clean.columns:
        duplicate_mail_rows = df_clean[df_clean.duplicated(subset=['mail_address'], keep='first')].copy()
        if not duplicate_mail_rows.empty:
            duplicate_mail_rows['Issue'] = 'Duplicate mail_address'
            invalid_rows = pd.concat([invalid_rows, duplicate_mail_rows], ignore_index=True)
        # Keep the first occurrence of each mail_address
        df_clean = df_clean.drop_duplicates(subset=['mail_address'], keep='first')

    # Step 6: Handle duplicate login_id (if the column exists)
    if 'login_id' in df_clean.columns:
        duplicate_login_rows = df_clean[df_clean.duplicated(subset=['login_id'], keep='first')].copy()
        if not duplicate_login_rows.empty:
            duplicate_login_rows['Issue'] = 'Duplicate login_id'
            invalid_rows = pd.concat([invalid_rows, duplicate_login_rows], ignore_index=True)
        # Keep the first occurrence of each login_id
        df_clean = df_clean.drop_duplicates(subset=['login_id'], keep='first')

    # Remove invalid records from the cleaned DataFrame
    invalid_rows = invalid_rows.drop_duplicates()

    return df_clean, invalid_rows

def load(df_cleaned, output_file, invalid_rows, garbage_file):
    if not df_cleaned.empty:
        # Save the cleaned DataFrame to a new CSV file
        df_cleaned.to_csv(output_file, index=False, encoding='utf-8')

    if not invalid_rows.empty:
        # Save the invalid/garbage records with the "Issue" column to a separate CSV file
        invalid_rows.to_csv(garbage_file, index=False, encoding='utf-8')
    return

import logging

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

try:
    # Extract, transform and load data
    df = extract(input_file)
    df_cleaned, invalid_rows = transform(df)
    load(df_cleaned, output_file,invalid_rows, garbage_file)

    logging.info("Data processing completed successfully.")

# Handle exceptions, log messages
except Exception as e:
    logging.error(f"An error occurred: {str(e)}")