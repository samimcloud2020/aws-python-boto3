pip install fastapi pydantic uvicorn

uvicorn main:app --reload

Access the API at http://127.0.0.1:8000 or test via Swagger UI at http://127.0.0.1:8000/docs

## POST:
curl -X POST "http://127.0.0.1:8000/items/" -H "Content-Type: application/json" -d '{"name":"Apple","price":1.99}'

## GET (all):
curl -X GET "http://127.0.0.1:8000/items/"

## GET (single):
curl -X GET "http://127.0.0.1:8000/items/{item_id}/"

## PUT:
curl -X PUT "http://127.0.0.1:8000/items/{item_id}/" -H "Content-Type: application/json" -d '{"name":"Updated Apple","price":2.99}'

## DELETE:
curl -X DELETE "http://127.0.0.1:8000/items/{item_id}/"
