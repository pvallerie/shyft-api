#!/bin/bash

curl "http://localhost:8000/bikes/${ID}" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
