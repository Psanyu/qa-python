# needed modules
import os
import mysql.connector
import pandas as pd
from google.cloud import bigquery

# variables
cur_path = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(cur_path, '../DataFiles')
load_file1 = 'MySQL.csv'
load_file = os.path.join(data_dir,load_file1)

proj = 'project-ad82d84d-c65a-4ed4-b00'
dataset = 'demo1'
table = 'annual_movie_summary'
table_id = f'{proj}.{dataset}.{table}'

# data connections
conn = mysql.connector.connect(option_files='C:/Users/pandi/QuerySurge/.my.cnf')
client = bigquery.Client(project=proj)

# extract is transformed via query (i.e. aggregation)
query = "select year " \
        ", count(distinct imdb_title_id) as movie_count " \
        ", avg(avg_vote) as avg_rating " \
        "from `u479841347_sql_course`.`imdb_movies` "\
        "where true " \
        "and year between 1940 and 2018 " \
        "group by 1"

# extract data
df = pd.read_sql(query, conn)

# transform data


def year_rating(x):
    if x <= 5.65:
        return 'bad movie year'
    elif x <= 5.9:
        return 'okay movie year'
    elif x <= 7:
        return 'great movie year'
    else:
        return 'not rated'


# transformation by derivation
df['year_rating'] = df['avg_rating'].apply(year_rating)
df.to_csv(load_file, index=False)

# load data
job_config = bigquery.LoadJobConfig(
    skip_leading_rows=1,
    source_format=bigquery.SourceFormat.CSV,
    autodetect=True,
    write_disposition='WRITE_TRUNCATE'
)

# open file for loading
with open(load_file, 'rb') as file:
    load_job = client.load_table_from_file(
        file,
        table_id,
        job_config=job_config
    )

load_job.result()

destination_table = client.get_table(table_id)
print("You have {} rows in your table.".format(destination_table.num_rows))