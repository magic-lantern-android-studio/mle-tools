#!/bin/bash

# For each Android Studio project, determine if there is anything that has been modified.
# Note that this is not an elegant solution since we are assuming that the name of the
# projects are the same as the github repository.

for i in core-math core-runtime parts-base parts-mrefs parts-roles parts-props parts-stages parts-sets parts-actors titles-imagetest titles-modeltest titles-hellocube;
do
    # Process Android project.
    echo $i;
    cd $i;

    # Use git status to flush state where diff-index was detecting files that do not
    # need to be committed (jar files touched by stagelibs.py script). Not sure why this works,
    # there may be an option on diff-index that could be used instead.
    git status > /dev/null;

    if git diff-index --name-status --exit-code HEAD;
    then
        echo "No update required.";
    else
        echo "Update required.";
    fi

    cd ..
    echo ""
done
