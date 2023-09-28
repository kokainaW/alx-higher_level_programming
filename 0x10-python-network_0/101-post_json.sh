#!/bin/bash
# Sends a JSON POST request to a URL passed as the first argument
curl -sX POST $1 -H "Content-Type: application/json" -d @$2 -L
