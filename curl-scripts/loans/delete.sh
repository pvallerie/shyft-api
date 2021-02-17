#!/bin/bash

curl "http://localhost:8000/loans/${ID}" \
  --include \
  --request DELETE \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}"

echo
