curl -X GET "http://library.demo.local/api/vl/books" -H "accept: application/json"
curl -X GET "http://library.demo.local/api/v1/books" -H "accept: application/json"
curl -X put "http://library.demo.local/api/v1/books" 
APIKEY = "cisco|5ds27q6PPuM7A7c3NMKnurggpoudPBjV9sTg_S0mNTA"
curl -X PUT "http://library.demo.local/api/v1/books/0" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"id\": 0, \"title\": \"1985\", \"author\": \"George Orwell\"}"

