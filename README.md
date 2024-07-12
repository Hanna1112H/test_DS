
## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Hanna1112H/currency-pipeline-
    cd currency_pipeline
    ```

2. Install the required libraries:
    ```bash
    pip install requests json zipfile datetime pandas matplotlib
    ```

## Prerequisites

Ensure you have the following libraries installed:
- `json`
- `zipfile`
- `datetime`
- `pandas`
- `matplotlib`

Place your ZIP file containing JSON files in the same directory as the script. Update the `zip_file_path` variable with the name of your ZIP file.

## Usage

### Extract and Read JSON Data

The script reads multiple JSON objects from each JSON file in the ZIP archive.

### Analyze Timestamps

- Timestamps are extracted, converted to datetime objects, and grouped by date.
- A bar plot is generated to visualize the count of records per date.

