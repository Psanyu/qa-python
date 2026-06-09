from google.cloud import bigquery

client = bigquery.Client(project='project-ad82d84d-c65a-4ed4-b00')

sql = "SELECT * FROM demo1.MoviesL"
query_job = client.query(sql)
result = query_job.result()

for row in result:
    print(row.year,row.title, row.duration, row.avg_vote)

    