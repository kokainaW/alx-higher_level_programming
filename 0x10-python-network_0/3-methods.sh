#!/bin/bash
# Script that takes in a URL and Displays all HTTP methods
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -f2- -d" "
