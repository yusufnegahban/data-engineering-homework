
#Question 4(week1). Longest trip for each day
```sql
SELECT 
    DATE(lpep_pickup_datetime) AS pickup_day,  
    MAX(trip_distance) AS longest_trip_distance  
FROM green_taxi_trips  
WHERE lpep_pickup_datetime >= '2019-10-01'  
  AND lpep_pickup_datetime < '2019-11-01'  
GROUP BY pickup_day  
ORDER BY longest_trip_distance DESC  
LIMIT 1;

```
+-----------------------+----------------------+
| zone                  | grand_total_amount   |
+-----------------------+----------------------+
| East Harlem North     | 18686.68             |
| East Harlem South     | 16797.26             |
| Morningside Heights   | 13029.79             |

```
Answer: `2019-10-31`
