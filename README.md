
## Installation

1. Clone the repository:
    ```bash
    git clone [https://github.com/Hanna1112H/currency-pipeline-](https://github.com/Hanna1112H/test_DS)
    cd test_DS
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

Place your ZIP file containing JSON files in the same directory as the script. Update the `json.zip` variable with the name of your ZIP file.
Please note json.zip file was added in my local version. Please use this code in your local due to github limits. 
My code analyze data from files and created answers for test tasks. 

## Usage

### Extract and Read JSON Data

The script reads multiple JSON objects from each JSON file in the ZIP archive.

### Analyze Timestamps

- Timestamps are extracted, converted to datetime objects, and grouped by date.
- A bar plot is generated to visualize the count of records per date.
Identify Sparse Variables:

The script calculates the percentage of missing values for each variable.
The top three most sparse variables are printed.

###Examine Regions and Ports:

The script identifies unique regions and ocean ports present in the data.
Frequency Analysis of Navigation Codes and Descriptions:

If columns navCode and NavDesc exist, the script performs frequency tabulations and prints the top 5 navigation codes and descriptions by percentage.

