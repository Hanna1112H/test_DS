import json
import zipfile
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
zip_file_path = 'json.zip'
all_data = []
def read_multiple_json_objects(file):
    objects = []
    data = file.read().decode('utf-8')
    for obj in data.split('\n'):
        if obj.strip():  
            objects.append(json.loads(obj))
    return objects
with zipfile.ZipFile(zip_file_path, 'r') as z:
    for file_info in z.infolist():
        if file_info.filename.endswith('.json'):
            with z.open(file_info.filename) as file:
                # Handle multiple JSON objects in the file
                data = read_multiple_json_objects(file)
                all_data.extend(data)
timestamps = [record['timestamp'] for record in all_data]
df = pd.DataFrame(timestamps, columns=['timestamp'])
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['date'] = df['timestamp'].dt.date
time_periods = df['date'].value_counts().sort_index()
time_periods.plot(kind='bar', figsize=(10, 5))
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('Main Time Periods in the Data')
plt.xticks(rotation=45)
plt.show()
#Which are the top three most sparse variables?
missing_variables = df.isnull().mean() * 100
sorted_missing_variables = missing_variables.sort_values(ascending=False)
top_three_sparse_variables = sorted_missing_variables.head(3)
print("Top three most sparse variables:\n", top_three_sparse_variables)
#What region(s) of the world and ocean port(s) does this data represent? 
df = pd.DataFrame(all_data)
unique_regions = df['region'].unique() if 'region' in df.columns else []
unique_ports = df['port'].unique() if 'port' in df.columns else []
print("Unique Regions:")
for region in unique_regions:
    print(region)
print("\nUnique Ports:")
for port in unique_ports:
    print(port)    
# Check if columns 'navCode' and 'NavDesc' exist and perform frequency tabulation
if 'navCode' in df.columns and 'NavDesc' in df.columns:
    # Frequency of navCode
    navcode_freq = df['navCode'].value_counts().reset_index()
    navcode_freq.columns = ['navCode', 'Frequency']
# Frequency of NavDesc
    navdesc_freq = df['NavDesc'].value_counts().reset_index()
    navdesc_freq.columns = ['NavDesc', 'Frequency']
print("Navigation Code Frequency:")
print(navcode_freq)
print("\nNavigation Description Frequency:")
print(navdesc_freq)
total_records = len(df)
navcode_freq['Percentage'] = (navcode_freq['Frequency'] / total_records) * 100
navdesc_freq['Percentage'] = (navdesc_freq['Frequency'] / total_records) * 100
print("\nTop 5 Navigation Codes by Percentage:")
print(navcode_freq.head())
print("\nTop 5 Navigation Descriptions by Percentage:")
print(navdesc_freq.head()) 
print("Columns 'navCode' and/or 'NavDesc' not found in the dataset.")        