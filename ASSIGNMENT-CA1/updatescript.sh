#!/bin/bash

# script by Eryk Gloginski to check for updates
# and if there is, update the system

echo "1234" | sudo -S apt-get update && sudo -S apt-get upgrade

echo "Successfully Updated! "