# BU KOD GOOGLE SHEET'TE KAYITLI OLAN DOSYAYI BIGQUERY'YE GÖNDERMEYE YARAR

from gspread_pandas import Spread, conf
import pandas_gbq
import os
import re

# spreadsheet ID and sheet name
spreadsheet_id =  '1da9oOVSfdxXX59m905pQ2Q2W7TIM6NowjvFG_VTumvY'
sheet_name = 'csv-to-google-sheet'

# your GCP project ID and GBQ destination table in format dataset.table
project_id = 'sniper-332121'
destination_table = 'eren_csv_data.google-sheet'

# get current directory
current_dir_path = os.path.dirname(os.path.realpath(__file__))

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = current_dir_path + '/google_secrets.json'
c = conf.get_config(current_dir_path, 'google_secrets.json')

spread = Spread(spreadsheet_id, config=c)

# get dataframe
df = spread.sheet_to_df(sheet=sheet_name, start_row=1).reset_index()


# function that will remove characters that are nor allowed by BigQuery in names of columns
def column_names_normalize(df):
    for col_name in df:
        all_except_letters = re.sub(r"([?!^a-zA-Z]+)", "_", col_name)
        remove_chars_at_beginning = col_name.lstrip(all_except_letters)
        new_col_name = re.sub(r"[^0-9a-zA-Z]+", "_", remove_chars_at_beginning)
        df.rename(columns={col_name: new_col_name}, inplace=True)
    return df


df = column_names_normalize(df)
print(df)

# upload data to BigQuery
pandas_gbq.to_gbq(df, destination_table, project_id, if_exists='replace')