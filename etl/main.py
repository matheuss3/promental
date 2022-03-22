import configparser
import pandas
from sqlalchemy import create_engine

def rename_column(df, old_name, new_name):
  df.rename(columns={old_name: new_name}, inplace=True)

config = configparser.ConfigParser()
config.read('config.ini')

dataset_path = config['DEFAULT']['dataset_csv']
df_in = pandas.read_csv(dataset_path, encoding="ISO-8859-1", delimiter=';')
print(df_in.head())

db_path = config['DEFAULT']['database']
engine = create_engine(f'sqlite:///{db_path}')

rename_column(df_in, 'dsm_mddh', 'possui_depressao')
rename_column(df_in, 'SAMPLEID', 'id')
df_out = df_in[['id', 'possui_depressao']]



df_out.to_sql('dataset_depressao', con=engine, if_exists='replace', index=False)