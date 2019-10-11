$!/bin/bash

if [ -z "$1" ]; then
  echo "you didnt provide an argument"
  exit 0;
fi
status=$(systemctl status $1 | grep Active | awk '{print $2}')
inactive="inactive"

if [ $status == inactive ]; then
  echo "noooooo it is off"
else
  echo "My status is $status"
fi
