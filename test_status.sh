$!/bin/bash

myvar=""

if [ -z "$1" ]; then
  exit 0;
fi
varname=$(systemctl status $1 | grep Active | awk '{print $2}')
varname2="inactive"

if [ $varname == $varname2 ]; then
  echo "noooooo it is off"
fi
