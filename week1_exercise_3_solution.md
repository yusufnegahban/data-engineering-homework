
#Question 3. Trip Segmentation Count
```sql
SELECT 
    CASE 
        WHEN trip_distance <= 1 THEN 'Up to 1 mile'
        WHEN trip_distance > 1 AND trip_distance <= 3 THEN '1~3 miles'
        WHEN trip_distance > 3 AND trip_distance <= 7 THEN '3~7 miles'
        WHEN trip_distance > 7 AND trip_distance <= 10 THEN '7~10 miles'
        ELSE '10+ miles'
    END AS segment,
    COUNT(*) AS num_trips
FROM green_taxi_trips
WHERE 
    lpep_pickup_datetime >= '2019-10-01' 
    AND lpep_pickup_datetime < '2019-11-01'
GROUP BY segment;

```
"segment"	"num_trips"
"10+ miles"	35201
"1~3 miles"	198995
"3~7 miles"	109642
"7~10 miles"	27686
"Up to 1 mile"	104830
```
Answer: `104,802; 198,924; 109,603; 27,678; 35,189`
