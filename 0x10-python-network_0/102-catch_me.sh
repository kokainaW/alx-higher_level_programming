#!/bin/bash
# Make a request to 0.0.0.0:5000/catch_me
curl -o /dev/null -sw "You got me!" 0.0.0.0:5000/catch_me
