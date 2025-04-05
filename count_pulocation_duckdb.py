import duckdb
from pathlib import Path

# Define the path to the folder containing the parquet files
folder = Path("D:/road map")

# List the months for which data is available (January to June)
months = ['01', '02', '03', '04', '05', '06']

# Generate a list of file paths for the parquet files of each month
files = [str(folder / f"yellow_tripdata_2024-{m}.parquet") for m in months]

# Create a query to count distinct PULocationIDs across all the specified files
query = f"""
SELECT COUNT(DISTINCT PULocationID) as unique_pu
FROM read_parquet({files})
"""

# Execute the query and get the result
result = duckdb.sql(query).fetchone()

# Print the number of unique PULocationIDs
print(f"Number of unique PULocationID: {result[0]}")



# Create a query to count the records where fare_amount is equal to 0 across all the parquet files
query = """
SELECT COUNT(*)
FROM read_parquet('D:/road map/yellow_tripdata_2024-*.parquet')
WHERE fare_amount = 0;
"""

# Execute the query and get the result
result = duckdb.sql(query).fetchone()

# Print the number of records where fare_amount equals 0
print(f"Number of records with fare_amount of 0: {result[0]}")




