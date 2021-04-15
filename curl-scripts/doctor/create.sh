#!/bin/bash

curl "http://localhost:8000/doctors/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Accept: application/json; indent=4" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "doctor": {
      "email": "'"${EMAIL}"'",
      "first_name": "'"${FNAME}"'",
      "last_name": "'"${LNAME}"'",
      "specialty": "'"${SPECIALTY}"'"
    }
  }'

echo
