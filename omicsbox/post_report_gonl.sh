curl -sS \
  -X POST \
  -H 'Content-Type: text/plain' \
  --data-binary @report_gonl.py \
  http://localhost:8000/run | jq -r '.stdout' | jq .
