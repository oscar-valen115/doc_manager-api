#!/bin/bash

curl "http://localhost:8000/doctors/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
