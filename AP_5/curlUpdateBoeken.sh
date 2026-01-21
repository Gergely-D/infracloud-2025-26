API_KEY="cisco|oPDek0hz2ppG3r0AH7ctns7ML4HtjFRir3Sq__gPix0"
ID=1001
TITLE="Two Towers   "
AUTHOR="JR Tolkien"
curl -X POST "http://library.demo.local/api/v1/books" \
-H "accept: application/json" \
-H "X-API-KEY: $API_KEY" \
-H "Content-Type: application/json" \
-d "{\"id\":$ID,\"title\":\"$TITLE\",\"author\":\"$AUTHOR\"}"