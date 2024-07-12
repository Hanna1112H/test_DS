# test-hanna
The Python code includes functionalities for reading multiple JSON objects from files, analyzing timestamps, identifying sparse variables, and examining geographical regions and ocean ports. Please note zip file was added in local version. Please add it in your local code due to github limits. 
Prerequisites
Ensure you have the following libraries installed:

'json
zipfile
datetime
pandas
matplotlib'

Place your ZIP file containing JSON files in the same directory as the script.
Place your ZIP file containing JSON files in the same directory as the script. Update the zip_file_path variable with the name of your ZIP file.

Steps:
Extract and Read JSON Data:

The script reads multiple JSON objects from each JSON file in the ZIP archive.

Analyze Timestamps:

Timestamps are extracted, converted to datetime objects, and grouped by date.
A bar plot is generated to visualize the count of records per date.

Identify Sparse Variables:

The script calculates the percentage of missing values for each variable.
The top three most sparse variables are printed.

Examine Regions and Ports:

The script identifies unique regions and ocean ports present in the data.
Frequency Analysis of Navigation Codes and Descriptions:

If columns navCode and NavDesc exist, the script performs frequency tabulations and prints the top 5 navigation codes and descriptions by percentage.
