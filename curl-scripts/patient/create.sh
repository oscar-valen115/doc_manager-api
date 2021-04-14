#!/bin/bash

curl "http://localhost:8000/patients/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "patient": {
      "email": "'"${EMAIL}"'",
      "first_name": "'"${FNAME}"'",
      "last_name": "'"${LNAME}"'",
      "dob": "'"${DOB}"'"
    }
  }'

echo
