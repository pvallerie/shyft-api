#!/bin/bash

curl "http://localhost:8000/bikes/${ID}" \
  --include \
  --request PATCH \
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
