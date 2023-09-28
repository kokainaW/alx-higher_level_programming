#!/bin/bash
# Script that sends a DELETE request to the URL passed as the first argument
curl -s "$1" -X DELETE
