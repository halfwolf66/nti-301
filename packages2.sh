#!/bin/bash
if [ -e /usr/bin/wget ]; then
  exit 0;
fi
yum -y install wget #installs wget
wget https://raw.githubusercontent.com/Sfenner/nti-300/master/package.txt
for packages in $(cat packages.txt); do
  yum -y install $packages
done
