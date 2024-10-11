# Lifebear Data Cleaner

This repository contains a Python script for cleaning and processing Lifebear user data from a CSV file. The script reads, processes, and outputs cleaned data and records that were removed during the process.

## Features

- **Input/Output Handling**: The script reads user data from a CSV file and outputs the cleaned data to a new CSV file.
- **Error Handling**: If there are issues with reading the input file (e.g., encoding issues), the script catches the exceptions and logs the error.
- **Data Cleaning**: Removes unwanted records and keeps track of those in a separate file for inspection.

## Requirements

- Python 3.x
- Pandas (`pip install pandas`)

## Files

- **Input File**: A CSV file containing raw data.
- **Output File**: Cleaned data saved as `cleaned_lifebear_8.csv`.
- **Garbage File**: Removed or invalid records saved as `RemovedRecords_8.csv`.

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/lifebear-cleaner.git
    ```
2. Install the dependencies:
    ```bash
    pip install pandas
    ```
3. Run the script:
    ```bash
    python lifebear.py
    ```

## Function Overview e.g

### `extract(input_file)`
This function is designed to read and return the data from a CSV file using `pandas`. Here’s how it works:

1. **Input Parameter:**
   - `input_file`: This is the file path to the CSV file you want to read. The function expects this to be passed as an argument when the function is called.

2. **Try-Except Block:**
   - The function uses a `try-except` block to handle any potential errors that might occur while trying to read the CSV file. This ensures that the program doesn't crash if something goes wrong (for example, a file not found or an encoding issue).
   
3. **Reading the CSV File:**
   - Inside the `try` block, the function uses the `pandas.read_csv()` method to read the CSV file into a pandas DataFrame.
   - The parameters used are:
     - `input_file`: The path to the CSV file that will be read.
     - `delimiter=';'`: This specifies that the delimiter used in the CSV file is a semicolon (`;`). It's important to define the correct delimiter because CSV files can use different delimiters (commas, semicolons, tabs, etc.).
     - `encoding='utf-8'`: This specifies that the file is encoded using UTF-8. This is a common character encoding that handles most characters and symbols correctly, but it can be adjusted depending on the file’s encoding.

4. **Return the DataFrame:**
   - If the file is read successfully, the function returns the pandas DataFrame (`df`), which contains all the data from the CSV file.

5. **Error Handling:**
   - If an error occurs while reading the file (for instance, if the file is missing or if there's an issue with the encoding), the `except` block will catch the error.
   - It prints a message to the console with the error details: `Error reading input file: {e}`. This allows you to see what went wrong without crashing the entire program.

