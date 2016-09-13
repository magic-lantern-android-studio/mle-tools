#!/usr/bin/python

# This script is used to build the Magic Lantern components and applications. After a successful build,
# the resulting artifacts (i.e. libraries and packages) will be staged into thier corresonding
# project locations.

import argparse
import os
import shutil
import tempfile
import subprocess

# Initialize project list.
g_projectSize = 11
g_projects = [None] * g_projectSize
g_projects[0] = "core-math"
g_projects[1] = 'core-runtime'
g_projects[2] = "parts-base"
g_projects[3] = "parts-mrefs"
g_projects[4] = "parts-roles"
g_projects[5] = "parts-props"
g_projects[6] = "parts-stages"
g_projects[7] = "parts-sets"
g_projects[8] = "parts-actors"
g_projects[9] = "titles-imagetest"
g_projects[10] = "titles-modeltest"

# List the available Magic Lantern projects to build.
def listProjects() :
    "This function prints the list of available Magic Lantern projects."
    for i in range(g_projectSize): 
        print g_projects[i]
    return

# Build a specific project library in batch mode.
def buildLibrary(project) :
    "This function builds a project library in batch mode."
    print "Building library " +  project + "..."
    cwd = os.getcwd()
    os.chdir(project)
    subprocess.check_call(['./gradlew', 'assembleDebug'])
    subprocess.check_call(['./gradlew', 'exportJar'])
    os.chdir(cwd)
    return

# Build a specific project library in batch mode.
def buildTitle(project) :
    "This function builds a project application in batch mode."
    print "Building title " +  project + "..."
    cwd = os.getcwd()
    os.chdir(project)
    subprocess.check_call(['./gradlew', 'assembleDebug'])
    os.chdir(cwd)
    return

# Retrieve the index into the project array.
def getIndex(project) :
    "This funtion gets the corresponding index in the project array for the specified project."
    for i in range(g_projectSize) :
        if g_projects[i] == project : break

    if i < g_projectSize :
        return i
    else :
        return -1

# Parse input arguments.
parser = argparse.ArgumentParser(description="Build Magic Lantern projects.")
parser.add_argument('project', choices=g_projects, help='project to build' )
args = parser.parse_args()

# Build selected project.
index = getIndex(args.project)
if index != -1 and index < 9 :
    buildLibrary(g_projects[index])
elif index >= 9 :
    buildTitle(g_projects[index])
