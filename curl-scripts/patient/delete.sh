#!/bin/bash

curl "http://localhost:8000/patients/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
