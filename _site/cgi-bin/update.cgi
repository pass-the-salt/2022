#!/bin/bash

# From https://theowinter.ch/articles/Use-cgi-bin-to-automate-Jekyll/

#Script is executed by www-data user. It needs to have write-access to
#/var/www/2022 & /var/www/2022-passthesalt/
echo "Content-type: text/plain"
echo
echo "Checking for updates to 2022..."
exec 2>&1
cd /var/www/2022

#Check if there are changes
if git checkout master &&
    git fetch origin master &&
    [ `git rev-list HEAD...origin/master --count` != 0 ] &&
    git merge origin/master
then
    echo 'Changes found, syncing.'
    #jekyll build
    rsync -av --delete /var/www/2022/_site/ /var/www/2022-passthesalt/
else
    echo 'Not updated.'
fi
echo "Have a nice day!"
