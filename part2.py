import json
import zipfile
from datetime import datetime
import pandas as pd
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
df = pd.DataFrame(all_data)
filtered_df = df[df['mmsi'] == 205792000]
top_nav_codes = filtered_df['navCode'].value_counts().head(5).index.tolist()
filtered_df = filtered_df[filtered_df['navCode'].isin(top_nav_codes)]
filtered_df.sort_values(by=['mmsi', 'timestamp'], inplace=True)
# Initialize variables to track contiguous series
current_nav_code = None
series_start_time = None
last_event_time = None
final_report = []
# Iterate through filtered data to find contiguous series
for index, row in filtered_df.iterrows():
    if row['navCode'] != current_nav_code:
        # Process the end of the previous series
        if current_nav_code is not None:
            lead_time = lead_time(series_start_time, last_event_time)
            final_report.append({
                'mmsi': row['mmsi'],
                'timestamp': last_event_time,
                'Navigation Code': current_nav_code,
                'Navigation Description': row['NavDesc'],
                'lead time (in Milliseconds)': lead_time
            })
# Start a new series
        current_nav_code = row['navCode']
        series_start_time = row['timestamp']
 # Update last event time for the current series
    last_event_time = row['timestamp']  
final_report_df = pd.DataFrame(final_report)
print("Final Report for MMSI = 205792000:")
print(final_report_df)                                         