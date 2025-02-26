```sql
SELECT
    z."Zone",
    ROUND(SUM(g.total_amount)::NUMERIC, 3) AS grand_total_amount
FROM green_taxi_trips g
INNER JOIN zones z ON g."PULocationID" = z."LocationID"
WHERE g.lpep_pickup_datetime::DATE = '2019-10-18'
GROUP BY z."Zone"
ORDER BY grand_total_amount DESC
LIMIT 3;

```
"Zone"	"grand_total_amount"
"East Harlem North"	18686.680
"East Harlem South"	16797.260
"Morningside Heights"	13029.790
```

