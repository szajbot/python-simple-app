## Logowanie do bazy z konsoli
psql -h localhost -d backend -p 5432 -U backenduser

## Uzytkownicy
l/p
email/asd
email2/asd2

# Curle ktróre mogą się przydać

## Dodanie ticketa do drivera

curl --location 'localhost:8000/tickets' \
--header 'Content-Type: application/json' \
--data '{
    "car_id": 1,
    "entrance_date": "1999-01-08 04:05:06"
}'
