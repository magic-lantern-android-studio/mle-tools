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
    if os.path.isdir('parts-base'):
        print "\tUpdating parts-base"
        shutil.copy('core-math/app/release/mlmath.jar', 'parts-base/app/libs/mlmath.jar')
    if os.path.isdir('parts-props'):
        print "\tUpdating parts-props"
        shutil.copy('core-math/app/release/mlmath.jar', 'parts-props/app/libs/mlmath.jar')
    if os.path.isdir('parts-roles'):
        print "\tUpdating parts-roles"
        shutil.copy('core-math/app/release/mlmath.jar', 'parts-roles/app/libs/mlmath.jar')
    if os.path.isdir('parts-sets'):
        print "\tUpdating parts-sets"
        shutil.copy('core-math/app/release/mlmath.jar', 'parts-sets/app/libs/mlmath.jar')
    if os.path.isdir('parts-stages'):
        print "\tUpdating parts-stages"
        shutil.copy('core-math/app/release/mlmath.jar', 'parts-stages/app/libs/mlmath.jar')
    if os.path.isdir('parts-actors'):
        print "\tUpdating parts-actors"
        shutil.copy('core-math/app/release/mlmath.jar', 'parts-actors/app/libs/mlmath.jar')
    if os.path.isdir('titles-imagetest'):
        print "\tUpdating titles-imagetest"
        shutil.copy('core-math/app/release/mlmath.jar', 'titles-imagetest/app/libs/mlmath.jar')
    if os.path.isdir('titles-modeltest'):
        print "\tUpdating titles-modeltest"
        shutil.copy('core-math/app/release/mlmath.jar', 'titles-modeltest/app/libs/mlmath.jar')
    if os.path.isdir('titles-hellocube'):
        print "\tUpdating titles-hellocube"
        shutil.copy('core-math/app/release/mlmath.jar', 'titles-hellocube/app/libs/mlmath.jar')
    if os.path.isdir('titles-cubetest'):
        print "\tUpdating titles-cubetest"
        shutil.copy('core-math/app/release/mlmath.jar', 'titles-cubetest/app/libs/mlmath.jar')
    return

# Stage core-runtime project.
def stageCoreRuntime() :
    print "Staging core-runtime...";
    if os.path.isdir('parts-actors'):
        print "\tUpdating parts-actors"
        shutil.copy('core-runtime/app/release/mlert.jar', 'parts-actors/app/libs/mlert.jar')
    if os.path.isdir('parts-base'):
        print "\tUpdating parts-base"
        shutil.copy('core-runtime/app/release/mlert.jar', 'parts-base/app/libs/mlert.jar')
    if os.path.isdir('parts-mrefs'):
        print "\tUpdating parts-mrefs"
        shutil.copy('core-runtime/app/release/mlert.jar', 'parts-mrefs/app/libs/mlert.jar')
    if os.path.isdir('parts-props'):
        print "\tUpdating parts-props"
        shutil.copy('core-runtime/app/release/mlert.jar', 'parts-props/app/libs/mlert.jar')
    if os.path.isdir('parts-roles'):
        print "\tUpdating parts-roles"
        shutil.copy('core-runtime/app/release/mlert.jar', 'parts-roles/app/libs/mlert.jar')
    if os.path.isdir('parts-sets'):
        print "\tUpdating parts-sets"
        shutil.copy('core-runtime/app/release/mlert.jar', 'parts-sets/app/libs/mlert.jar')
    if os.path.isdir('parts-stages'):
        print "\tUpdating parts-stages"
        shutil.copy('core-runtime/app/release/mlert.jar', 'parts-stages/app/libs/mlert.jar')
    if os.path.isdir('titles-imagetest'):
        print "\tUpdating titles-imagetest"
        shutil.copy('core-runtime/app/release/mlert.jar', 'titles-imagetest/app/libs/mlert.jar')
    if os.path.isdir('titles-modeltest'):
        print "\tUpdating titles-modeltest"
        shutil.copy('core-runtime/app/release/mlert.jar', 'titles-modeltest/app/libs/mlert.jar')
    if os.path.isdir('titles-hellocube'):
        print "\tUpdating titles-hellocube"
        shutil.copy('core-runtime/app/release/mlert.jar', 'titles-hellocube/app/libs/mlert.jar')
    if os.path.isdir('titles-cubetest'):
        print "\tUpdating titles-cubetest"
        shutil.copy('core-runtime/app/release/mlert.jar', 'titles-cubetest/app/libs/mlert.jar')
    return

# Stage parts-base project.
def stagePartsBase() :
    print "Staging parts-base...";
    if os.path.isdir('parts-actors'):
        print "\tUpdating parts-actors"
        shutil.copy('parts-base/app/release/parts.jar', 'parts-actors/app/libs/parts.jar')
    if os.path.isdir('parts-mrefs'):
        print "\tUpdating parts-mrefs"
        shutil.copy('parts-base/app/release/parts.jar', 'parts-mrefs/app/libs/parts.jar')
        shutil.copy('parts-base/min3d/build/outputs/aar/min3d-debug.aar', 'parts-mrefs/min3d-debug/min3d-debug.aar')
    if os.path.isdir('parts-props'):
        print "\tUpdating parts-props"
        shutil.copy('parts-base/app/release/parts.jar', 'parts-props/app/libs/parts.jar')
    if os.path.isdir('parts-roles'):
        print "\tUpdating parts-roles"
        shutil.copy('parts-base/app/release/parts.jar', 'parts-roles/app/libs/parts.jar')
        shutil.copy('parts-base/min3d/build/outputs/aar/min3d-debug.aar', 'parts-roles/min3d-debug/min3d-debug.aar')
    if os.path.isdir('parts-sets'):
        print "\tUpdating parts-sets"
        shutil.copy('parts-base/app/release/parts.jar', 'parts-sets/app/libs/parts.jar')
    if os.path.isdir('parts-stages'):
        print "\tUpdating parts-stages"
        shutil.copy('parts-base/app/release/parts.jar', 'parts-stages/app/libs/parts.jar')
    if os.path.isdir('titles-imagetest'):
        print "\tUpdating titles-imagetest"
        shutil.copy('parts-base/app/release/parts.jar', 'titles-imagetest/app/libs/parts.jar')
    if os.path.isdir('titles-modeltest'):
        print "\tUpdating titles-modeltest"
        shutil.copy('parts-base/app/release/parts.jar', 'titles-modeltest/app/libs/parts.jar')
        shutil.copy('parts-base/min3d/build/outputs/aar/min3d-debug.aar', 'titles-modeltest/min3d-debug/min3d-debug.aar')
    if os.path.isdir('titles-hellocube'):
        print "\tUpdating titles-hellocube"
        shutil.copy('parts-base/app/release/parts.jar', 'titles-hellocube/app/libs/parts.jar')
        shutil.copy('parts-base/min3d/build/outputs/aar/min3d-debug.aar', 'titles-hellocube/min3d-debug/min3d-debug.aar')
    if os.path.isdir('titles-cubetest'):
        print "\tUpdating titles-cubetest"
        shutil.copy('parts-base/app/release/parts.jar', 'titles-cubetest/app/libs/parts.jar')
        shutil.copy('parts-base/min3d/build/outputs/aar/min3d-debug.aar', 'titles-cubetest/min3d-debug/min3d-debug.aar')
    if os.path.isdir('test-min3d_01'):
        print "\tUpdating test-min3d_01"
        shutil.copy('parts-base/min3d/build/outputs/aar/min3d-debug.aar', 'test-min3d_01/min3d-debug/min3d-debug.aar')
    if os.path.isdir('test-min3d_02'):
        print "\tUpdating test-min3d_02"
        shutil.copy('parts-base/min3d/build/outputs/aar/min3d-debug.aar', 'test-min3d_02/min3d-debug/min3d-debug.aar')
    return

# Stage parts-mrefs project.
def stagePartsMrefs() :
    print "Staging parts-mrefs...";
    if os.path.isdir('parts-actors'):
        print "\tUpdating parts-actors"
        shutil.copy('parts-mrefs/app/release/mrefs.jar', 'parts-actors/app/libs/mrefs.jar')
    if os.path.isdir('parts-roles'):
        print "\tUpdating parts-roles"
        shutil.copy('parts-mrefs/app/release/mrefs.jar', 'parts-roles/app/libs/mrefs.jar')
    if os.path.isdir('titles-imagetest'):
        print "\tUpdating titles-imagetest"
        shutil.copy('parts-mrefs/app/release/mrefs.jar', 'titles-imagetest/app/libs/mrefs.jar')
    if os.path.isdir('titles-modeltest'):
        print "\tUpdating titles-modeltest"
        shutil.copy('parts-mrefs/app/release/mrefs.jar', 'titles-modeltest/app/libs/mrefs.jar')
    if os.path.isdir('titles-hellocube'):
        print "\tUpdating titles-hellocube"
        shutil.copy('parts-mrefs/app/release/mrefs.jar', 'titles-hellocube/app/libs/mrefs.jar')
    if os.path.isdir('titles-cubetest'):
        print "\tUpdating titles-cubetest"
        shutil.copy('parts-mrefs/app/release/mrefs.jar', 'titles-cubetest/app/libs/mrefs.jar')
    return

# Stage parts-roles project.
def stagePartsRoles() :
    print "Staging parts-roles...";
    if os.path.isdir('parts-props'):
        print "\tUpdating parts-props"
        shutil.copy('parts-roles/app/release/roles.jar', 'parts-props/app/libs/roles.jar')
    if os.path.isdir('parts-sets'):
        print "\tUpdating parts-sets"
        shutil.copy('parts-roles/app/release/roles.jar', 'parts-sets/app/libs/roles.jar')
    if os.path.isdir('titles-imagetest'):
        print "\tUpdating titles-imagetest"
        shutil.copy('parts-roles/app/release/roles.jar', 'titles-imagetest/app/libs/roles.jar')
    if os.path.isdir('titles-modeltest'):
        print "\tUpdating titles-modeltest"
        shutil.copy('parts-roles/app/release/roles.jar', 'titles-modeltest/app/libs/roles.jar')
    if os.path.isdir('titles-hellocube'):
        print "\tUpdating titles-hellocube"
        shutil.copy('parts-roles/app/release/roles.jar', 'titles-hellocube/app/libs/roles.jar')
    if os.path.isdir('titles-cubetest'):
        print "\tUpdating titles-cubetest"
        shutil.copy('parts-roles/app/release/roles.jar', 'titles-cubetest/app/libs/roles.jar')
    return

# Stage parts-props project.
def stagePartsProps() :
    print "Staging parts-props...";
    if os.path.isdir('parts-actors'):
        print "\tUpdating parts-actors"
        shutil.copy('parts-props/app/release/props.jar', 'parts-actors/app/libs/props.jar')
    if os.path.isdir('titles-imagetest'):
        print "\tUpdating titles-imagetest"
        shutil.copy('parts-props/app/release/props.jar', 'titles-imagetest/app/libs/props.jar')
    if os.path.isdir('titles-modeltest'):
        print "\tUpdating titles-modeltest"
        shutil.copy('parts-props/app/release/props.jar', 'titles-modeltest/app/libs/props.jar')
    if os.path.isdir('titles-hellocube'):
        print "\tUpdating titles-hellocube"
        shutil.copy('parts-props/app/release/props.jar', 'titles-hellocube/app/libs/props.jar')
    if os.path.isdir('titles-cubetest'):
        print "\tUpdating titles-cubetest"
        shutil.copy('parts-props/app/release/props.jar', 'titles-cubetest/app/libs/props.jar')
    return

# Stage parts-stages project.
def stagePartsStages() :
    print "Staging parts-stages...";
    if os.path.isdir('parts-sets'):
        print "\tUpdating parts-sets"
        shutil.copy('parts-stages/app/release/stages.jar', 'parts-sets/app/libs/stages.jar')
    if os.path.isdir('titles-imagetest'):
        print "\tUpdating titles-imagetest"
        shutil.copy('parts-stages/app/release/stages.jar', 'titles-imagetest/app/libs/stages.jar')
    if os.path.isdir('titles-modeltest'):
        print "\tUpdating titles-modeltest"
        shutil.copy('parts-stages/app/release/stages.jar', 'titles-modeltest/app/libs/stages.jar')
    if os.path.isdir('titles-hellocube'):
        print "\tUpdating titles-hellocube"
        shutil.copy('parts-stages/app/release/stages.jar', 'titles-hellocube/app/libs/stages.jar')
    if os.path.isdir('titles-cubetest'):
        print "\tUpdating titles-cubetest"
        shutil.copy('parts-stages/app/release/stages.jar', 'titles-cubetest/app/libs/stages.jar')
    return

# Stage parts-sets project.
def stagePartsSets() :
    print "Staging parts-sets...";
    if os.path.isdir('titles-imagetest'):
        print "\tUpdating titles-imagetest"
        shutil.copy('parts-sets/app/release/sets.jar', 'titles-imagetest/app/libs/sets.jar')
    if os.path.isdir('titles-modeltest'):
        print "\tUpdating titles-modeltest"
        shutil.copy('parts-sets/app/release/sets.jar', 'titles-modeltest/app/libs/sets.jar')
    if os.path.isdir('titles-hellocube'):
        print "\tUpdating titles-hellocube"
        shutil.copy('parts-sets/app/release/sets.jar', 'titles-hellocube/app/libs/sets.jar')
    if os.path.isdir('titles-cubetest'):
        print "\tUpdating titles-cubetest"
        shutil.copy('parts-sets/app/release/sets.jar', 'titles-cubetest/app/libs/sets.jar')
    return

# Stage parts-actors project.
def stagePartsActors() :
    print "Staging parts-actors...";
    if os.path.isdir('titles-imagetest'):
        print "\tUpdating titles-imagetest"
        shutil.copy('parts-actors/app/release/actors.jar', 'titles-imagetest/app/libs/actors.jar')
    if os.path.isdir('titles-modeltest'):
        print "\tUpdating titles-modeltest"
        shutil.copy('parts-actors/app/release/actors.jar', 'titles-modeltest/app/libs/actors.jar')
    if os.path.isdir('titles-hellocube'):
        print "\tUpdating titles-hellocube"
        shutil.copy('parts-actors/app/release/actors.jar', 'titles-hellocube/app/libs/actors.jar')
    if os.path.isdir('titles-cubetest'):
        print "\tUpdating titles-cubetest"
        shutil.copy('parts-actors/app/release/actors.jar', 'titles-cubetest/app/libs/actors.jar')
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
