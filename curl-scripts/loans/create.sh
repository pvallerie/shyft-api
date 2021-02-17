#!/bin/bash

curl "http://localhost:8000/loans" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "loan": {
      "pickup_date": "'"${PICKUPDATE}"'",
      "dropoff_date": "'"${DROPOFFDATE}"'",
      "bike": "'"${BIKE}"'"
    }
  }'

echo
