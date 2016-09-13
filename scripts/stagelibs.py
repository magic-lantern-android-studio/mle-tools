#!/usr/bin/python

# This script is used to stage the Magic Lantern Core and Parts libraries into their
# corresponding Android Studio projects.

import os
import shutil
import tempfile
import argparse

# Initialize project list.
g_projectSize = 10
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
g_projects[9] = "all"

# List the available Magic Lantern projects to stage.
def listProjects() :
    "This function prints the list of available Magic Lantern projects."
    for i in range(g_projectSize):
        print g_projects[i]
    return

# Stage core-math project.
def stageCoreMath() :
    print "Staging core-math...";
    print "\tUpdating parts-props"
    if os.path.isdir('parts-props'):
        shutil.copy('core-math/app/release/mlmath.jar', 'parts-props/app/libs/mlmath.jar')
    print "\tUpdating parts-roles"
    if os.path.isdir('parts-roles'):
        shutil.copy('core-math/app/release/mlmath.jar', 'parts-roles/app/libs/mlmath.jar')
    print "\tUpdating parts-sets"
    if os.path.isdir('parts-sets'):
        shutil.copy('core-math/app/release/mlmath.jar', 'parts-sets/app/libs/mlmath.jar')
    print "\tUpdating parts-stages"
    if os.path.isdir('parts-stages'):
        shutil.copy('core-math/app/release/mlmath.jar', 'parts-stages/app/libs/mlmath.jar')
    print "\tUpdating parts-actors"
    if os.path.isdir('parts-actors'):
        shutil.copy('core-math/app/release/mlmath.jar', 'parts-actors/app/libs/mlmath.jar')
    print "\tUpdating titles-imagetest"
    if os.path.isdir('titles-imagetest'):
        shutil.copy('core-math/app/release/mlmath.jar', 'titles-imagetest/app/libs/mlmath.jar')
    print "\tUpdating titles-modeltest"
    if os.path.isdir('titles-modeltest'):
        shutil.copy('core-math/app/release/mlmath.jar', 'titles-modeltest/app/libs/mlmath.jar')
    return

# Stage core-runtime project.
def stageCoreRuntime() :
    print "Staging core-runtime...";
    print "\tUpdating parts-actors"
    if os.path.isdir('parts-actors'):
        shutil.copy('core-runtime/app/release/mlert.jar', 'parts-actors/app/libs/mlert.jar')
    print "\tUpdating parts-base"
    if os.path.isdir('parts-base'):
        shutil.copy('core-runtime/app/release/mlert.jar', 'parts-base/app/libs/mlert.jar')
    print "\tUpdating parts-mrefs"
    if os.path.isdir('parts-mrefs'):
        shutil.copy('core-runtime/app/release/mlert.jar', 'parts-mrefs/app/libs/mlert.jar')
    print "\tUpdating parts-props"
    if os.path.isdir('parts-props'):
        shutil.copy('core-runtime/app/release/mlert.jar', 'parts-props/app/libs/mlert.jar')
    print "\tUpdating parts-roles"
    if os.path.isdir('parts-roles'):
        shutil.copy('core-runtime/app/release/mlert.jar', 'parts-roles/app/libs/mlert.jar')
    print "\tUpdating parts-sets"
    if os.path.isdir('parts-sets'):
        shutil.copy('core-runtime/app/release/mlert.jar', 'parts-sets/app/libs/mlert.jar')
    print "\tUpdating parts-stages"
    if os.path.isdir('parts-stages'):
        shutil.copy('core-runtime/app/release/mlert.jar', 'parts-stages/app/libs/mlert.jar')
    print "\tUpdating titles-imagetest"
    if os.path.isdir('titles-imagetest'):
        shutil.copy('core-runtime/app/release/mlert.jar', 'titles-imagetest/app/libs/mlert.jar')
    print "\tUpdating titles-modeltest"
    if os.path.isdir('titles-modeltest'):
        shutil.copy('core-runtime/app/release/mlert.jar', 'titles-modeltest/app/libs/mlert.jar')
    return

# Stage parts-base project.
def stagePartsBase() :
    print "Staging parts-base...";
    print "\tUpdating parts-actors"
    if os.path.isdir('parts-actors'):
        shutil.copy('parts-base/app/release/parts.jar', 'parts-actors/app/libs/parts.jar')
    print "\tUpdating parts-mrefs"
    if os.path.isdir('parts-mrefs'):
        shutil.copy('parts-base/app/release/parts.jar', 'parts-mrefs/app/libs/parts.jar')
    print "\tUpdating parts-props"
    if os.path.isdir('parts-props'):
        shutil.copy('parts-base/app/release/parts.jar', 'parts-props/app/libs/parts.jar')
    print "\tUpdating parts-roles"
    if os.path.isdir('parts-roles'):
        shutil.copy('parts-base/app/release/parts.jar', 'parts-roles/app/libs/parts.jar')
    print "\tUpdating parts-sets"
    if os.path.isdir('parts-sets'):
        shutil.copy('parts-base/app/release/parts.jar', 'parts-sets/app/libs/parts.jar')
    print "\tUpdating parts-stages"
    if os.path.isdir('parts-stages'):
        shutil.copy('parts-base/app/release/parts.jar', 'parts-stages/app/libs/parts.jar')
    print "\tUpdating titles-imagetest"
    if os.path.isdir('titles-imagetest'):
        shutil.copy('parts-base/app/release/parts.jar', 'titles-imagetest/app/libs/parts.jar')
    print "\tUpdating titles-modeltest"
    if os.path.isdir('titles-modeltest'):
        shutil.copy('parts-base/app/release/parts.jar', 'titles-modeltest/app/libs/parts.jar')
    return

# Stage parts-mrefs project.
def stagePartsMrefs() :
    print "Staging parts-mrefs...";
    print "\tUpdating parts-actors"
    if os.path.isdir('parts-actors'):
        shutil.copy('parts-mrefs/app/release/mrefs.jar', 'parts-actors/app/libs/mrefs.jar')
    print "\tUpdating parts-roles"
    if os.path.isdir('parts-roles'):
        shutil.copy('parts-mrefs/app/release/mrefs.jar', 'parts-roles/app/libs/mrefs.jar')
    print "\tUpdating titles-imagetest"
    if os.path.isdir('titles-imagetest'):
        shutil.copy('parts-mrefs/app/release/mrefs.jar', 'titles-imagetest/app/libs/mrefs.jar')
    print "\tUpdating titles-modeltest"
    if os.path.isdir('titles-modeltest'):
        shutil.copy('parts-mrefs/app/release/mrefs.jar', 'titles-modeltest/app/libs/mrefs.jar')
    return

# Stage parts-roles project.
def stagePartsRoles() :
    print "Staging parts-roles...";
    print "\tUpdating parts-roles"
    if os.path.isdir('parts-props'):
        shutil.copy('parts-roles/app/release/roles.jar', 'parts-props/app/libs/roles.jar')
    print "\tUpdating parts-props"
    if os.path.isdir('parts-sets'):
        shutil.copy('parts-roles/app/release/roles.jar', 'parts-sets/app/libs/roles.jar')
    print "\tUpdating titles-imagetest"
    if os.path.isdir('titles-imagetest'):
        shutil.copy('parts-roles/app/release/roles.jar', 'titles-imagetest/app/libs/roles.jar')
    print "\tUpdating titles-modeltest"
    if os.path.isdir('titles-modeltest'):
        shutil.copy('parts-roles/app/release/roles.jar', 'titles-modeltest/app/libs/roles.jar')
    return

# Stage parts-props project.
def stagePartsProps() :
    print "Staging parts-props...";
    print "\tUpdating parts-props"
    if os.path.isdir('parts-actors'):
        shutil.copy('parts-props/app/release/props.jar', 'parts-actors/app/libs/props.jar')
    print "\tUpdating titles-imagetest"
    if os.path.isdir('titles-imagetest'):
        shutil.copy('parts-props/app/release/props.jar', 'titles-imagetest/app/libs/props.jar')
    print "\tUpdating titles-modeltest"
    if os.path.isdir('titles-modeltest'):
        shutil.copy('parts-props/app/release/props.jar', 'titles-modeltest/app/libs/props.jar')
    return

# Stage parts-stages project.
def stagePartsStages() :
    print "Staging parts-stages...";
    print "\tUpdating parts-staeges"
    if os.path.isdir('parts-sets'):
        shutil.copy('parts-stages/app/release/stages.jar', 'parts-sets/app/libs/stages.jar')
    print "\tUpdating titles-imagetest"
    if os.path.isdir('titles-imagetest'):
        shutil.copy('parts-stages/app/release/stages.jar', 'titles-imagetest/app/libs/stages.jar')
    print "\tUpdating titles-modeltest"
    if os.path.isdir('titles-modeltest'):
        shutil.copy('parts-stages/app/release/stages.jar', 'titles-modeltest/app/libs/stages.jar')
    return

# Stage parts-sets project.
def stagePartsSets() :
    print "Staging parts-sets...";
    print "\tUpdating titles-imagetest"
    if os.path.isdir('titles-imagetest'):
        shutil.copy('parts-sets/app/release/sets.jar', 'titles-imagetest/app/libs/sets.jar')
    print "\tUpdating titles-modeltest"
    if os.path.isdir('titles-modeltest'):
        shutil.copy('parts-sets/app/release/sets.jar', 'titles-modeltest/app/libs/sets.jar')
    return

# Stage parts-actors project.
def stagePartsActors() :
    print "Staging parts-actors...";
    print "\tUpdating titles-imagetest"
    if os.path.isdir('titles-imagetest'):
        shutil.copy('parts-actors/app/release/actors.jar', 'titles-imagetest/app/libs/actors.jar')
    print "\tUpdating titles-modeltest"
    if os.path.isdir('titles-modeltest'):
        shutil.copy('parts-actors/app/release/actors.jar', 'titles-modeltest/app/libs/actors.jar')
    return

# Parse input arguments.
parser = argparse.ArgumentParser(description="Stage Magic Lantern projects.")
parser.add_argument('project', choices=g_projects, help='project to stage' )
args = parser.parse_args()

# Stage select project.
if args.project == "core-math" :
    stageCoreMath()
elif args.project == "core-runtime" :
    stageCoreRuntime()
elif args.project == "parts-base" :
    stagePartsBase()
elif args.project == "parts-mrefs" :
    stagePartsMrefs()
elif args.project == "parts-roles" :
    stagePartsRoles()
elif args.project == "parts-props" :
    stagePartsProps()
elif args.project == "parts-sets" :
    stagePartsSets()
elif args.project == "parts-stages" :
    stagePartsStages()
elif args.project == "parts-actors" :
    stagePartsActors()
else :
    stageCoreMath()
    stageCoreRuntime()
    stagePartsBase()
    stagePartsMrefs()
    stagePartsRoles()
    stagePartsProps()
    stagePartsStages()
    stagePartsSets()
    stagePartsActors()

print "...Done"
