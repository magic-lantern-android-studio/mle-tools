#!/bin/bash

# For each Android Studio project, build the Debug variant and stage the
# library.

# Note that this is not an elegant solution since we are assuming that the
# name of the projects are the same as the github repository.

for i in core-math core-runtime parts-base parts-mrefs parts-roles parts-props parts-stages parts-sets parts-actors;
do
    # Process Android project.
    echo "============================================================"
    echo Building $i;
    echo ""
    cd $i;

    # Build Debug
    ./gradlew assembleDebug
    ./gradlew exportJar

    # Stage library
    echo ""
    echo Staging $i
    ../mle-tools/scripts/stagelibs.py

    cd ..
    echo ""
done

for i in titles-imagetest titles-modeltest;
do
    # Process Android project.
    echo "============================================================"
    echo Building $i;
    echo ""
    cd $i;

    # Builde Debug
    ./gradlew assembleDebug

    cd ..
    echo ""
done