#!/bin/sh

# This script needs to be executed from the directory where the git repos
# have been cloned.
#
# Tip: use "ssh-add ~/.ssh/id_rsa" to add your SSH key to the ssh-agent so
# you dont have to give your passphrase every time "git diff" in invoked.

echo " ***** Processing core-math *****"
cd core-math
git diff --exit-code > /dev/null
rc=$?
if [[ $rc != 0 ]]
then
    echo "There are local, unstaged changes."
fi
git diff --cached --exit-code > /dev/null
rc=$?
if [[ $rc != 0 ]]
then
    echo "There are changes staged, but not committed."
fi

echo " ***** Processing core-runtime *****"
cd ../core-runtime
git diff --exit-code > /dev/null
rc=$?
if [[ $rc != 0 ]]
then
    echo "There are local, unstaged changes."
fi
git diff --cached --exit-code > /dev/null
rc=$?
if [[ $rc != 0 ]]
then
    echo "There are changes staged, but not committed."
fi

echo " ***** Processing parts-base *****"
cd ../parts-base
git diff --exit-code > /dev/null
rc=$?
if [[ $rc != 0 ]]
then
    echo "There are local, unstaged changes."
fi
git diff --cached --exit-code > /dev/null
rc=$?
if [[ $rc != 0 ]]
then
    echo "There are changes staged, but not committed."
fi

echo " ***** Processing parts-props *****"
cd ../parts-props
git diff --exit-code > /dev/null
rc=$?
if [[ $rc != 0 ]]
then
    echo "There are local, unstaged changes."
fi
git diff --cached --exit-code > /dev/null
rc=$?
if [[ $rc != 0 ]]
then
    echo "There are changes staged, but not committed."
fi

echo " ***** Processing parts-mrefs *****"
cd ../parts-mrefs
git diff --exit-code > /dev/null
rc=$?
if [[ $rc != 0 ]]
then
    echo "There are local, unstaged changes."
fi
git diff --cached --exit-code > /dev/null
rc=$?
if [[ $rc != 0 ]]
then
    echo "There are changes staged, but not committed."
fi

echo " ***** Processing parts-roles *****"
cd ../parts-roles
git diff --exit-code > /dev/null
rc=$?
if [[ $rc != 0 ]]
then
    echo "There are local, unstaged changes."
fi
git diff --cached --exit-code > /dev/null
rc=$?
if [[ $rc != 0 ]]
then
    echo "There are changes staged, but not committed."
fi

echo " ***** Processing parts-sets *****"
cd ../parts-sets
git diff --exit-code > /dev/null
rc=$?
if [[ $rc != 0 ]]
then
    echo "There are local, unstaged changes."
fi
git diff --cached --exit-code > /dev/null
rc=$?
if [[ $rc != 0 ]]
then
    echo "There are changes staged, but not committed."
fi

echo " ***** Processing parts-stages *****"
cd ../parts-stages
git diff --exit-code > /dev/null
rc=$?
if [[ $rc != 0 ]]
then
    echo "There are local, unstaged changes."
fi
git diff --cached --exit-code > /dev/null
rc=$?
if [[ $rc != 0 ]]
then
    echo "There are changes staged, but not committed."
fi

echo " ***** Processing parts-actors *****"
cd ../parts-actors
git diff --exit-code > /dev/null
rc=$?
if [[ $rc != 0 ]]
then
    echo "There are local, unstaged changes."
fi
git diff --cached --exit-code > /dev/null
rc=$?
if [[ $rc != 0 ]]
then
    echo "There are changes staged, but not committed."
fi

echo " ***** Processing titles-imagetest *****"
cd ../titles-imagetest
git diff --exit-code > /dev/null
rc=$?
if [[ $rc != 0 ]]
then
    echo "There are local, unstaged changes."
fi
git diff --cached --exit-code > /dev/null
rc=$?
if [[ $rc != 0 ]]
then
    echo "There are changes staged, but not committed."
fi

echo " ***** Processing titles-cubetest *****"
cd ../titles-cubetest
git diff --exit-code > /dev/null
rc=$?
if [[ $rc != 0 ]]
then
    echo "There are local, unstaged changes."
fi
git diff --cached --exit-code > /dev/null
rc=$?
if [[ $rc != 0 ]]
then
    echo "There are changes staged, but not committed."
fi

echo " ***** Processing titles-hellocube *****"
cd ../titles-hellocube
git diff --exit-code > /dev/null
rc=$?
if [[ $rc != 0 ]]
then
    echo "There are local, unstaged changes."
fi
git diff --cached --exit-code > /dev/null
rc=$?
if [[ $rc != 0 ]]
then
    echo "There are changes staged, but not committed."
fi

echo " ***** Processing titles-modeltest *****"
cd ../titles-modeltest
git diff --exit-code > /dev/null
rc=$?
if [[ $rc != 0 ]]
then
    echo "There are local, unstaged changes."
fi
git diff --cached --exit-code > /dev/null
rc=$?
if [[ $rc != 0 ]]
then
    echo "There are changes staged, but not committed."
fi

echo " ***** Processing titles-movietest *****"
cd ../titles-movietest
git diff --exit-code > /dev/null
rc=$?
if [[ $rc != 0 ]]
then
    echo "There are local, unstaged changes."
fi
git diff --cached --exit-code > /dev/null
rc=$?
if [[ $rc != 0 ]]
then
    echo "There are changes staged, but not committed."
fi

echo " ***** Processing mle-documentation *****"
cd ../mle-documentation
git diff --exit-code > /dev/null
rc=$?
if [[ $rc != 0 ]]
then
    echo "There are local, unstaged changes."
fi
git diff --cached --exit-code > /dev/null
rc=$?
if [[ $rc != 0 ]]
then
    echo "There are changes staged, but not committed."
fi

cd ..
