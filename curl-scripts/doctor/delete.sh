#!/bin/bash

curl "http://localhost:8000/doctors/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
