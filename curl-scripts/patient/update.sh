#!/bin/bash

curl "http://localhost:8000/patients/${ID}/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Accept: application/json; indent=4" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "patient": {
      "first_name": "'"${FNAME}"'",
      "last_name": "'"${LNAME}"'",
      "email": "'"${EMAIL}"'",
      "dob": "'"${DOB}"'",
      "street_address": "'"${SADDRESS}"'",
      "city": "'"${CITY}"'",
      "state": "'"${STATE}"'",
      "allergies": "'"${ALLERGIES}"'"
    }
  }'

echo
