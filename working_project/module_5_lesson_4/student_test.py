import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/student_test_db", pool_recycle=-1)

print('engine created successful')

df = pd.read_csv('student_test.csv', index_col=0)
print(df)

df.to_sql('student_test', con=engine, if_exists='append', index=False)
print('loaded successful')