import os
import pandas as pd 
from dotenv import load_dotenv
from sqlalchemy import create_engine, types


df = pd.read_csv('DataCo_SupplyChain_Cleaned_Final.csv')


df.columns = [c.replace(' ', '_').replace('(', '').replace(')', '').replace('-', '_').strip() for c in df.columns]


sql_types = {}
for col in df.columns:
    if df[col].dtype == 'int64':
        sql_types[col] = types.INTEGER()
    elif df[col].dtype == 'float64':
        sql_types[col] = types.Float(precision=4)
    else:
        max_len = max(df[col].astype(str).str.len().max(), 50) 
        sql_types[col] = types.VARCHAR(length=int(max_len + 20))


load_dotenv()

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")


connection_string = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"
engine = create_engine(connection_string)

df.to_sql(
    name='supply_chain_analytics', 
    con=engine, 
    if_exists='replace', 
    index=False, 
    dtype=sql_types, 
    chunksize=5000
)
