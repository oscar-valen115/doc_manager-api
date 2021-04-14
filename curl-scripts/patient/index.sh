#!/bin/bash

curl "http://localhost:8000/patients/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
