#!/bin/bash
# Script that takes in a URL as an argument, sends a GET request
curl -s "$1" -H "X-School-User-Id: 98"
