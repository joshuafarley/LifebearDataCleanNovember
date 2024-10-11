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

## Function Overview

### `extract(input_file)`
Reads the input CSV file and returns a DataFrame. Handles any potential errors during the reading process.

## Customization

You can modify the `input_file`, `output_file`, and `garbage_file` paths at the beginning of the script to work with your own data files.

## Contributing

Feel free to fork this repository, submit issues, or create pull requests to enhance the functionality of this script.

## License

This project is licensed under the MIT License.
