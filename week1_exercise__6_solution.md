```sql
SELECT
    puz."Zone" AS pickup_zone,
    doz."Zone" AS dropoff_zone,
    g.tip_amount
FROM
    green_taxi_trips g
INNER JOIN
    zones puz ON g."PULocationID" = puz."LocationID"
INNER JOIN
    zones doz ON g."DOLocationID" = doz."LocationID"
WHERE
    puz."Zone" = 'East Harlem North'
ORDER BY
    g.tip_amount DESC
LIMIT 1;


```
+-------------------+---------------------+------------+
| pickup_zone       | dropoff_zone        | tip_amount |
|-------------------+---------------------+------------|
| East Harlem North | JFK Airport         | 87.3       

```

Answer: `JFK Airport`