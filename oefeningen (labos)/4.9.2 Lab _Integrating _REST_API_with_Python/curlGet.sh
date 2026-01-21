curl -X POST http://library.demo.local/api/v1/books \
-H "Content-Type: application/json" \
-H "X-API-Key: cisco|oPDek0hz2ppG3r0AH7ctns7ML4HtjFRir3Sq__gPix0" \
-d '{
  "id": 888,
  "title": "Test Book",
  "author": "Cisco DevNet",
  "isbn": "9780134190440"
}'