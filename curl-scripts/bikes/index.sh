#!/bin/bash

curl "http://localhost:8000/bikes" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
