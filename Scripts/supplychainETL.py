import pandas as pd 
from sqlalchemy import create_engine , types


df = pd.read_csv(r"C:\Users\ASUS\Desktop\PaperTradeX\DataCo_SupplyChain_Cleaned_Final.csv")
print(df)

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



engine = create_engine("mysql+pymysql://root:root123@localhost/supplychain_data")


df.to_sql(
    name='supply_chain_analytics', 
    con=engine, 
    if_exists='replace', 
    index=False, 
    dtype=sql_types, 
    chunksize=5000
)
