from google.cloud import bigquery
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"/Users/halil/Documents/Eren/Task_3/python_bq_private_key.json"

client = bigquery.Client()
table_id = "local-receiver-356716.GoogleSheetCSV.GoogleSheetData"
file_path = r"/Users/halil/Documents/Eren/Task_3/tft_20220711.csv"

job_config = bigquery.LoadJobConfig(
    source_format = bigquery.SourceFormat.CSV , skip_leading_rows = 1, autodetect=True,
        write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE
)

with open(file_path, "rb") as source_file:
    job = client.load_table_from_file(source_file, table_id, job_config = job_config)

table = client.get_table(table_id)
print(
    "{} satır ve {} sütun {}' ye eklendi.".format(table.num_rows, len(table.schema), table_id)
)