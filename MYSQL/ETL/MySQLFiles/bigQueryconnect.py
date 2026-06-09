from google.cloud import bigquery

client = bigquery.Client(project="project-ad82d84d-c65a-4ed4-b00")

df = client.query("""
    SELECT * FROM `bigquery-public-data.thelook_ecommerce.orders`
    LIMIT 10
""").to_dataframe()

print(df.head())