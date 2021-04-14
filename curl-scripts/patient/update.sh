#!/bin/bash

curl "http://localhost:8000/patients/${ID}/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Accept: application/json; indent=4" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "mango": {
      "name": "'"${NAME}"'",
      "color": "'"${COLOR}"'",
      "ripe": "'"${RIPE}"'"
    }
  }'

echo
