import time
import pandas as pd

# Load the dataset
file_path = 'WarehouseProject/Sample_Dataset.csv'  
df = pd.read_csv(file_path)

current_timestamp_seconds = int(time.time())
print(current_timestamp_seconds)

def simulate_real_time_data(df, limit=20):
    counter = 0
    for index, row in df.iterrows():
        if counter >= limit:
            break
        # Simulate real-time data point generation
        print(f"id: {current_timestamp_seconds + row['Time']}, battery_voltage: {row['Battery Voltage (V)']}, battery_current: {row['Battery Current (A)']}")
        time.sleep(1)  # Wait for 1 second to simulate real-time ingestion
        counter += 1

if __name__ == "__main__":
    simulate_real_time_data(df)

import time
import pandas as pd
import boto3

# Load the dataset
file_path = 'WarehouseProject/Sample_Dataset.csv'  
df = pd.read_csv(file_path)

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

# Your DynamoDB table name
table_name = "WarehouseRobotLogs"

current_timestamp_seconds = int(time.time())
print(current_timestamp_seconds)

def simulate_real_time_data(df, limit=1):
    counter = 0
    for index, row in df.iterrows():
        if counter >= limit:
            break
        
        # Generate the current timestamp for each iteration
        current_time = current_timestamp_seconds + row['Time']
        
        # Simulate real-time data point generation
        print(f"id: {current_time}, battery_voltage: {row['Battery Voltage (V)']}, battery_current: {row['Battery Current (A)']}")
        
        # Insert data into DynamoDB
        dynamodb.put_item(
            TableName=table_name,
            Item={
                    'id': {'N': '1'},
                    'battery_voltage': {'N': '38.66'},
                    'battery_current': {'N': '369'}
                }
        )
        
        # Wait for 1 second to simulate real-time ingestion
        time.sleep(1)
        counter += 1

if __name__ == "__main__":
    simulate_real_time_data(df)