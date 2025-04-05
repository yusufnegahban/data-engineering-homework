import duckdb
from pathlib import Path

folder = Path("D:/road map")
months = ['01', '02', '03', '04', '05', '06']
files = [str(folder / f"yellow_tripdata_2024-{m}.parquet") for m in months]

# ساخت query با استفاده از آرایه فایل‌ها
query = f"""
SELECT COUNT(DISTINCT PULocationID) as unique_pu
FROM read_parquet({files})
"""

result = duckdb.sql(query).fetchone()
print(f"تعداد PULocationID یکتا: {result[0]}")




# اجرای کوئری برای تعداد رکوردهای fare_amount برابر با 0
query = """
SELECT COUNT(*)
FROM read_parquet('D:/road map/yellow_tripdata_2024-*.parquet')
WHERE fare_amount = 0;
"""

# اجرای کوئری و گرفتن نتیجه
result = duckdb.sql(query).fetchone()

# چاپ تعداد رکوردهای fare_amount برابر با 0
print(f"Number of records with fare_amount of 0: {result[0]}")



