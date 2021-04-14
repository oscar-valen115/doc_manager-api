#!/bin/bash

curl "http://localhost:8000/doctors/${ID}/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
