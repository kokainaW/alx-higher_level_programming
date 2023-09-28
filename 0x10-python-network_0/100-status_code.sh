#!/bin/bash
# Sends a request to a URL passed as an argument, and displays
curl -o /dev/null -sw "%{http_code}" $1
