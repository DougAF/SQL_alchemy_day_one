import pandas as pd
import os
from sqlalchemy import create_engine, inspect

census_db_path = os.path.join("..", "Resources", "Census_Data.sqlite")
zip_db_path = os.path.join("..", "Resources", "Zip_Census.sqlite")

census_engine = create_engine(f"sqlite:///{census_db_path}")
zip_engine = create_engine(f"sqlite:///{zip_db_path}")

census_inspector = inspect(census_engine)
zip_inspector = inspect(zip_engine)

#table_names = census_inspector.get_table_names()

#print(table_names)
table_names = zip_inspector.get_table_names()

print(table_names)
# schema = census_inspector.get_columns("Census_Data")
# # print(schema)
# # print()
# schema = zip_inspector.get_columns("Zip_Census")
# # print(schema)
# # census_df = pd.read_sql_query("SELECT * FROM Census_Data", con=census_engine)
# # zip_df = pd.read_sql_query("SELECT * FROM Zip_Census", con=zip_engine)
# census_df = pd.read_sql_table("Census_Data", con=census_engine)
# zip_df = pd.read_sql_table("Zip_Census", con=zip_engine)
# # print(census_df)
# # print("*" * 50)
# # print(zip_df)
# df = pd.merge(census_df, zip_df, on="CityState")
# print(df)