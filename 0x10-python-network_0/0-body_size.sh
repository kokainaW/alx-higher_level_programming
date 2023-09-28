#!/bin/bash
# Takes in a URL, Sends a request to that URL, and Displays
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
