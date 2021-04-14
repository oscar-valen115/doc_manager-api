#!/bin/bash

curl "http://localhost:8000/patients/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}" \
  --header "Accept: application/json; indent=4" \

echo
