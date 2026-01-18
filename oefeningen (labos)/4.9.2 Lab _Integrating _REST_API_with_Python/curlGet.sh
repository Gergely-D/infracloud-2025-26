curl -X POST http://library.demo.local/api/v1/books \
-H "Content-Type: application/json" \
-H "X-API-Key: <TOKEN>" \
-d '{
  "id": 900,
  "title": "Test Book",
  "author": "Cisco DevNet",
  "isbn": "9780134190440"
}'