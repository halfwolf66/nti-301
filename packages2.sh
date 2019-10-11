#!/bin/bash
yum -y install wget
wget https://raw.githubusercontent.com/Sfenner/nti-300/master/package.txt
for packages in $(cat packages.txt); do
  yum -y install $packages
done
