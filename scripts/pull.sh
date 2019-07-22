#!/bin/sh

# This script needs to be executed from the directory where the git repos
# have been cloned.
#
# Tip: use "ssh-add ~/.ssh/id_rsa" to add your SSH key to the ssh-agent so
# you dont have to give your passphrase every time "git pull" in invoked.

echo " ***** Processing mle-tools *****"
cd mle-tools
git pull

echo " ***** Processing core-math *****"
cd ../core-math
git pull

echo " ***** Processing core-runtime *****"
cd ../core-runtime
git pull

echo " ***** Processing parts-base *****"
cd ../parts-base
git pull

echo " ***** Processing parts-mrefs *****"
cd ../parts-mrefs
git pull

echo " ***** Processing parts-props *****"
cd ../parts-props
git pull

echo " ***** Processing parts-roles *****"
cd ../parts-roles
git pull

echo " ***** Processing parts-sets *****"
cd ../parts-sets
git pull

echo " ***** Processing parts-stages *****"
cd ../parts-stages
git pull

echo " ***** Processing parts-actors *****"
cd ../parts-actors
git pull

echo " ***** Processing titles-imagetest *****"
cd ../titles-imagetest
git pull

echo " ***** Processing titles-cubetest *****"
cd ../titles-cubetest
git pull

echo " ***** Processing titles-modeltest *****"
cd ../titles-modeltest
git pull

echo " ***** Processing titles-hellocube *****"
cd ../titles-hellocube
git pull

echo " ***** Processing mle-documentation *****"
cd ../mle-documentation
git pull

cd ..
