
select
    case
        when trip_distance <= 1 then 'Up to 1 mile'
        when trip_distance > 1 and trip_distance <= 3 then '1~3 miles'
        when trip_distance > 3 and trip_distance <= 7 then '3~7 miles'
        when trip_distance > 7 and trip_distance <= 10 then '7~10 miles'
        else '10+ miles'
    end as segment,
    to_char(count(1), '999,999') as num_trips
from
    green_taxi_trips
where
    lpep_pickup_datetime >= '2019-10-01'
    and lpep_pickup_datetime < '2019-11-01'
    and lpep_dropoff_datetime >= '2019-10-01'
    and lpep_dropoff_datetime < '2019-11-01'
group by
    segment