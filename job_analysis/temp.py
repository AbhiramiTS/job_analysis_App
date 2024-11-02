# import pandas as pd
# from sqlalchemy import create_engine

# # Load CSV file
# file_path = r'C:\Users\My Account\Downloads\Job Analysis\job-listing-analysis\updated_data\job_industries.csv'
# df = pd.read_csv(file_path)

# # Create engine and connect to PostgreSQL
# engine = create_engine('postgresql+psycopg2://postgres:abhi123@localhost:5432/Job Analysis')

# # Load data into PostgreSQL
# df.to_sql('app_jobindustry', engine, if_exists='append', index=False)



# import pandas as pd
# from sqlalchemy import create_engine

# # Load CSV file
# file_path = r'C:\Users\My Account\Downloads\Job Analysis\job-listing-analysis\updated_data\employee_counts.csv'
# df = pd.read_csv(file_path)

# # Assuming your CSV has the following columns:
# # 'company_id', 'employee_count', 'follower_count', 'time_recorded'
# # You may need to rename these columns if they differ.

# # Convert 'time_recorded' from Unix timestamp to datetime if necessary
# df['time_recorded'] = pd.to_datetime(df['time_recorded'], unit='s')

# # Ensure the DataFrame's column types match your Django model
# df['employee_count'] = df['employee_count'].astype(int)
# df['follower_count'] = df['follower_count'].astype(int)

# # Create engine and connect to PostgreSQL
# engine = create_engine('postgresql+psycopg2://postgres:abhi123@localhost:5432/Job Analysis')

# # Load data into PostgreSQL with chunksize for large datasets
# try:
#     df.to_sql('app_companymetrics', engine, if_exists='append', index=False, chunksize=1000)
# except Exception as e:
#     print(f"An error occurred: {e}")




# import pandas as pd
# import numpy as np
# from sqlalchemy import create_engine

# # Connect to your database
# engine = create_engine('postgresql+psycopg2://postgres:abhi123@localhost:5432/Job Analysis')

# # Load your DataFrame
# df = pd.read_csv(r'C:\Users\My Account\Downloads\Job Analysis\job-listing-analysis\updated_data\salaries.csv')

# # Step 1: Get valid job IDs from the database
# valid_job_ids = pd.read_sql("SELECT job_id FROM app_job", engine)['job_id'].tolist()

# # Step 2: Shuffle the valid job IDs
# np.random.shuffle(valid_job_ids)

# # Step 3: Replace job_id in df
# num_rows = len(df)
# num_valid_ids = len(valid_job_ids)

# if num_rows > num_valid_ids:
#     # If df is larger than valid job IDs, repeat valid job IDs
#     # Here we use numpy to ensure we have enough IDs
#     repeated_ids = np.tile(valid_job_ids, int(np.ceil(num_rows / num_valid_ids)))
#     df['job_id'] = repeated_ids[:num_rows]  # Truncate to the size of df
# else:
#     # If df is smaller or equal, just slice the shuffled valid IDs
#     df['job_id'] = valid_job_ids[:num_rows]

# # Step 4: Insert the modified DataFrame back to the database
# try:
#     df.to_sql('app_salary', engine, if_exists='append', index=False)
# except Exception as e:
#     print(f"Error occurred: {e}")




import pandas as pd
from sqlalchemy import create_engine

# Load CSV file
file_path = r'C:\Users\My Account\Downloads\Job Analysis\job-listing-analysis\updated_data\benefits.csv'
df = pd.read_csv(file_path)

# Create engine and connect to PostgreSQL
engine = create_engine('postgresql+psycopg2://postgres:abhi123@localhost:5432/Job Analysis')


# Get existing company IDs
existing_job_ids = pd.read_sql('SELECT job_id FROM app_job', engine)


# Filter DataFrame
df_filtered = df[df['job_id'].isin(existing_job_ids['job_id'])]

print(df)

# Load data into PostgreSQL
try:
    df_filtered.to_sql('app_benefits', engine, if_exists='append', index=False)
except Exception as e:
    print("An error occurred:", e)



# import pandas as pd
# from sqlalchemy import create_engine

# # Load CSV file
# file_path = r'C:\Users\My Account\Downloads\Job Analysis\job-listing-analysis\updated_data\company.csv'
# df = pd.read_csv(file_path)

# # Check the maximum lengths of the relevant columns
# max_lengths = df[['state', 'country', 'city', 'zip_code', 'address', 'url']].applymap(lambda x: len(x) if isinstance(x, str) else 0).max()
# print(max_lengths)

# # Truncate columns if necessary
# df['state'] = df['state'].str.slice(0, 100)
# df['country'] = df['country'].str.slice(0, 100)
# df['city'] = df['city'].str.slice(0, 100)
# df['zip_code'] = df['zip_code'].str.slice(0, 20)
# df['address'] = df['address'].str.slice(0, 255)
# df['url'] = df['url'].str.slice(0, 255)

# # Create engine and connect to PostgreSQL
# engine = create_engine('postgresql+psycopg2://postgres:abhi123@localhost:5432/Job Analysis')

# # Try to load data into PostgreSQL
# try:
#     df.to_sql('app_company', engine, if_exists='append', index=False)
# except Exception as e:
#     print("Error occurred:", e)


import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection string
pg_conn_string = "postgresql+psycopg2://postgres:abhi123@localhost:5432/Job Analysis"
# SQLite connection string
sqlite_conn_string = "sqlite:///db.sqlite3"

# Create connection to PostgreSQL
pg_engine = create_engine(pg_conn_string)

# Load data from PostgreSQL
df = pd.read_sql("SELECT * FROM app_benefits", pg_engine)

# Create connection to SQLite
sqlite_engine = create_engine(sqlite_conn_string)

# Write data to SQLite
df.to_sql('app_benefits', sqlite_engine, if_exists='replace', index=False)

print("Data copied successfully!")
