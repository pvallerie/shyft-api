#!/bin/bash

curl "http://localhost:8000/loans" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
