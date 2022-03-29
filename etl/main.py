import configparser
import pandas
from sqlalchemy import create_engine
import json


def rename_column(df, old_name, new_name):
  df.rename(columns={old_name: new_name}, inplace=True)

# Read config file
config = configparser.ConfigParser()
config.read('config.ini')

# Read dataset and create pandas dataframe
dataset_path = config['DEFAULT']['dataset_csv']
df_in = pandas.read_csv(dataset_path, encoding="ISO-8859-1", delimiter=';')

# Database connection
db_path = config['DEFAULT']['database']
engine = create_engine(f'sqlite:///{db_path}')

# Read variables mapper
path_file_vars = config['DEFAULT']['variables']
file_vars = open(path_file_vars)
map_vars = json.load(file_vars)


# Update name and select columns mapped
columns_mapped = []
for element in map_vars:
  rename_column(df_in, element['source_name'], element['alt_name'])

  for lst_value in element['replace']:
    df_in.replace({element['alt_name']: lst_value[0]}, {element['alt_name']: lst_value[1]}, inplace=True)

  columns_mapped.append(element['alt_name'])

df_out = df_in[columns_mapped]



df_out.to_sql('dataset_depressao', con=engine, if_exists='replace', index=False)