#!/bin/bash

curl "http://localhost:8000/bikes" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "bike": {
      "name": "'"${NAME}"'",
      "type": "'"${TYPE}"'",
      "size": "'"${SIZE}"'",
      "location": "'"${LOCATION}"'"
    }
  }'

echo
