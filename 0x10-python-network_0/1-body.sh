#!/bin/bash
# Takes in a URL, sends a request to that URL, and displays
curl -sX GET $1 -L
