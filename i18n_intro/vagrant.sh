#!/bin/bash

echo -n "Installing dependencies..."

sudo apt-get -qq update
sudo apt-get -qq -y install python-dev python-setuptools build-essential gettext
sudo easy_install pip 2>&1 > /dev/null
sudo pip install virtualenv 2>&1 > /dev/null
virtualenv /home/vagrant/.project_ve 2>&1 > /dev/null
if [ -e /mnt/project/requirements.txt ] ; then
    echo -n "Building virtualenv..."
    /home/vagrant/.project_ve/bin/pip install -r /mnt/project/requirements.txt 2>&1 > /dev/null
fi

if [[ "project" != *"`cat /home/vagrant/.bashrc`" ]] ; then
    echo "source ~/.project_ve/bin/activate && cd /mnt/project" >> /home/vagrant/.bashrc
fi
echo -n "Done."
