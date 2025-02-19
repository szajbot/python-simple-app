psql -h localhost -d backend -p 5432 -U backenduser

curl --location 'localhost:8000/tickets' \
--header 'Content-Type: application/json' \
--data '{
    "car_id": 1,
    "entrance_date": "1999-01-08 04:05:06"
}'

walidacje na jeden aktywny bilet na danym car

poprawić endpoionty

