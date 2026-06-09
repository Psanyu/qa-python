from google.cloud import bigquery
from googleapiclient.discovery_cache import autodetect
import os

client = bigquery.Client(project='project-ad82d84d-c65a-4ed4-b00')

target_table='project-ad82d84d-c65a-4ed4-b00.demo1.cityhousing'

job_config = bigquery.LoadJobConfig(
    skip_leading_rows=1,
    source_format=bigquery.SourceFormat.CSV,
autodetect=True,
write_disposition='WRITE_TRUNCATE')

curpath = os.path.dirname(__file__)
file5 = 'CitiesL.csv'
filepath5 = os.path.join(curpath, '../DataFiles', file5)

with open(filepath5,'rb') as source_file:
    load_job = client.load_table_from_file(source_file,target_table,job_config=job_config)
    load_job.result()

destination_table = client.get_table(target_table)
print(f"You have {destination_table.num_rows} rows in your table")



    