#!/bin/bash

curl "http://localhost:8000/doctors/${ID}/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --header "Accept: application/json; indent=4" \
  --data '{
    "doctor": {
      "email": "'"${EMAIL}"'",
      "first_name": "'"${FNAME}"'",
      "last_name": "'"${LNAME}"'",
      "specialty": "'"${SPECIALTY}"'"
    }
  }'

echo
