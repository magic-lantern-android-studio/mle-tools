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
        if not os.path.exists('parts-base/app/libs'):
            os.makedirs('parts-base/app/libs')
        shutil.copy('core-math/app/release/mlmath.jar', 'parts-base/app/libs/mlmath.jar')
        shutil.copy('core-math/app/release/mlmath-sources.jar', 'parts-base/app/libs/mlmath-sources.jar')
    if os.path.isdir('parts-props'):
        print "\tUpdating parts-props"
        if not os.path.exists('parts-props/app/libs'):
            os.makedirs('parts-props/app/libs')
        shutil.copy('core-math/app/release/mlmath.jar', 'parts-props/app/libs/mlmath.jar')
        shutil.copy('core-math/app/release/mlmath-sources.jar', 'parts-props/app/libs/mlmath-sources.jar')
    if os.path.isdir('parts-roles'):
        print "\tUpdating parts-roles"
        if not os.path.exists('parts-roles/app/libs'):
            os.makedirs('parts-roles/app/libs')
        shutil.copy('core-math/app/release/mlmath.jar', 'parts-roles/app/libs/mlmath.jar')
        shutil.copy('core-math/app/release/mlmath-sources.jar', 'parts-roles/app/libs/mlmath-sources.jar')
    if os.path.isdir('parts-sets'):
        print "\tUpdating parts-sets"
        if not os.path.exists('parts-sets/app/libs'):
            os.makedirs('parts-sets/app/libs')
        shutil.copy('core-math/app/release/mlmath.jar', 'parts-sets/app/libs/mlmath.jar')
        shutil.copy('core-math/app/release/mlmath-sources.jar', 'parts-sets/app/libs/mlmath-sources.jar')
    if os.path.isdir('parts-stages'):
        print "\tUpdating parts-stages"
        if not os.path.exists('parts-stages/app/libs'):
            os.makedirs('parts-stages/app/libs')
        shutil.copy('core-math/app/release/mlmath.jar', 'parts-stages/app/libs/mlmath.jar')
        shutil.copy('core-math/app/release/mlmath-sources.jar', 'parts-stages/app/libs/mlmath-sources.jar')
    if os.path.isdir('parts-actors'):
        print "\tUpdating parts-actors"
        if not os.path.exists('parts-actors/app/libs'):
            os.makedirs('parts-actors/app/libs')
        shutil.copy('core-math/app/release/mlmath.jar', 'parts-actors/app/libs/mlmath.jar')
        shutil.copy('core-math/app/release/mlmath-sources.jar', 'parts-actors/app/libs/mlmath-sources.jar')
    if os.path.isdir('titles-imagetest'):
        print "\tUpdating titles-imagetest"
        if not os.path.exists('titles-imagetest/app/libs'):
            os.makedirs('titles-imagetest/app/libs')
        shutil.copy('core-math/app/release/mlmath.jar', 'titles-imagetest/app/libs/mlmath.jar')
        shutil.copy('core-math/app/release/mlmath-sources.jar', 'titles-imagetest/app/libs/mlmath-sources.jar')
    if os.path.isdir('titles-modeltest'):
        print "\tUpdating titles-modeltest"
        if not os.path.exists('titles-modeltest/app/libs'):
            os.makedirs('titles-modeltest/app/libs')
        shutil.copy('core-math/app/release/mlmath.jar', 'titles-modeltest/app/libs/mlmath.jar')
        shutil.copy('core-math/app/release/mlmath-sources.jar', 'titles-modeltest/app/libs/mlmath-sources.jar')
    if os.path.isdir('titles-hellocube'):
        print "\tUpdating titles-hellocube"
        if not os.path.exists('titles-hellocube/app/libs'):
            os.makedirs('titles-hellocube/app/libs')
        shutil.copy('core-math/app/release/mlmath.jar', 'titles-hellocube/app/libs/mlmath.jar')
        shutil.copy('core-math/app/release/mlmath-sources.jar', 'titles-hellocube/app/libs/mlmath-sources.jar')
    if os.path.isdir('titles-cubetest'):
        print "\tUpdating titles-cubetest"
        if not os.path.exists('titles-cubetest/app/libs'):
            os.makedirs('titles-cubetest/app/libs')
        shutil.copy('core-math/app/release/mlmath.jar', 'titles-cubetest/app/libs/mlmath.jar')
        shutil.copy('core-math/app/release/mlmath-sources.jar', 'titles-cubetest/app/libs/mlmath-sources.jar')
    if os.path.isdir('titles-movietest'):
        print "\tUpdating titles-movietest"
        if not os.path.exists('titles-movietest/app/libs'):
            os.makedirs('titles-movietest/app/libs')
        shutil.copy('core-math/app/release/mlmath.jar', 'titles-movietest/app/libs/mlmath.jar')
        shutil.copy('core-math/app/release/mlmath-sources.jar', 'titles-movietest/app/libs/mlmath-sources.jar')
    return

# Stage core-runtime project.
def stageCoreRuntime() :
    print "Staging core-runtime...";
    if os.path.isdir('parts-actors'):
        print "\tUpdating parts-actors"
        if not os.path.exists('parts-actors/app/libs'):
            os.makedirs('parts-actors/app/libs')
        shutil.copy('core-runtime/app/release/mlert.jar', 'parts-actors/app/libs/mlert.jar')
        shutil.copy('core-runtime/app/release/mlert-sources.jar', 'parts-actors/app/libs/mlert-sources.jar')
    if os.path.isdir('parts-base'):
        print "\tUpdating parts-base"
        if not os.path.exists('parts-base/app/libs'):
            os.makedirs('parts-base/app/libs')
        shutil.copy('core-runtime/app/release/mlert.jar', 'parts-base/app/libs/mlert.jar')
        shutil.copy('core-runtime/app/release/mlert-sources.jar', 'parts-base/app/libs/mlert-sources.jar')
    if os.path.isdir('parts-mrefs'):
        print "\tUpdating parts-mrefs"
        if not os.path.exists('parts-mrefs/app/libs'):
            os.makedirs('parts-mrefs/app/libs')
        shutil.copy('core-runtime/app/release/mlert.jar', 'parts-mrefs/app/libs/mlert.jar')
        shutil.copy('core-runtime/app/release/mlert-sources.jar', 'parts-mrefs/app/libs/mlert-sources.jar')
    if os.path.isdir('parts-props'):
        print "\tUpdating parts-props"
        if not os.path.exists('parts-props/app/libs'):
            os.makedirs('parts-props/app/libs')
        shutil.copy('core-runtime/app/release/mlert.jar', 'parts-props/app/libs/mlert.jar')
        shutil.copy('core-runtime/app/release/mlert-sources.jar', 'parts-props/app/libs/mlert-sources.jar')
    if os.path.isdir('parts-roles'):
        print "\tUpdating parts-roles"
        if not os.path.exists('parts-roles/app/libs'):
            os.makedirs('parts-roles/app/libs')
        shutil.copy('core-runtime/app/release/mlert.jar', 'parts-roles/app/libs/mlert.jar')
        shutil.copy('core-runtime/app/release/mlert-sources.jar', 'parts-roles/app/libs/mlert-sources.jar')
    if os.path.isdir('parts-sets'):
        print "\tUpdating parts-sets"
        if not os.path.exists('parts-sets/app/libs'):
            os.makedirs('parts-sets/app/libs')
        shutil.copy('core-runtime/app/release/mlert.jar', 'parts-sets/app/libs/mlert.jar')
        shutil.copy('core-runtime/app/release/mlert-sources.jar', 'parts-sets/app/libs/mlert-sources.jar')
    if os.path.isdir('parts-stages'):
        print "\tUpdating parts-stages"
        if not os.path.exists('parts-stages/app/libs'):
            os.makedirs('parts-stages/app/libs')
        shutil.copy('core-runtime/app/release/mlert.jar', 'parts-stages/app/libs/mlert.jar')
        shutil.copy('core-runtime/app/release/mlert-sources.jar', 'parts-stages/app/libs/mlert-sources.jar')
    if os.path.isdir('titles-imagetest'):
        print "\tUpdating titles-imagetest"
        if not os.path.exists('titles-imagetest/app/libs'):
            os.makedirs('titles-imagetest/app/libs')
        shutil.copy('core-runtime/app/release/mlert.jar', 'titles-imagetest/app/libs/mlert.jar')
        shutil.copy('core-runtime/app/release/mlert-sources.jar', 'titles-imagetest/app/libs/mlert-sources.jar')
    if os.path.isdir('titles-modeltest'):
        print "\tUpdating titles-modeltest"
        if not os.path.exists('titles-modeltest/app/libs'):
            os.makedirs('titles-modeltest/app/libs')
        shutil.copy('core-runtime/app/release/mlert.jar', 'titles-modeltest/app/libs/mlert.jar')
        shutil.copy('core-runtime/app/release/mlert-sources.jar', 'titles-modeltest/app/libs/mlert-sources.jar')
    if os.path.isdir('titles-hellocube'):
        print "\tUpdating titles-hellocube"
        if not os.path.exists('titles-hellocube/app/libs'):
            os.makedirs('titles-hellocube/app/libs')
        shutil.copy('core-runtime/app/release/mlert.jar', 'titles-hellocube/app/libs/mlert.jar')
        shutil.copy('core-runtime/app/release/mlert-sources.jar', 'titles-hellocube/app/libs/mlert-sources.jar')
    if os.path.isdir('titles-cubetest'):
        print "\tUpdating titles-cubetest"
        if not os.path.exists('titles-cubetest/app/libs'):
            os.makedirs('titles-cubetest/app/libs')
        shutil.copy('core-runtime/app/release/mlert.jar', 'titles-cubetest/app/libs/mlert.jar')
        shutil.copy('core-runtime/app/release/mlert-sources.jar', 'titles-cubetest/app/libs/mlert-sources.jar')
    if os.path.isdir('titles-movietest'):
        print "\tUpdating titles-movietest"
        if not os.path.exists('titles-movietest/app/libs'):
            os.makedirs('titles-movietest/app/libs')
        shutil.copy('core-runtime/app/release/mlert.jar', 'titles-movietest/app/libs/mlert.jar')
        shutil.copy('core-runtime/app/release/mlert-sources.jar', 'titles-movietest/app/libs/mlert-sources.jar')
    return

# Stage parts-base project.
def stagePartsBase() :
    print "Staging parts-base...";
    if os.path.isdir('parts-actors'):
        print "\tUpdating parts-actors"
        if not os.path.exists('parts-actors/app/libs'):
            os.makedirs('parts-actors/app/libs')
        shutil.copy('parts-base/app/release/parts.jar', 'parts-actors/app/libs/parts.jar')
        shutil.copy('parts-base/app/release/parts-sources.jar', 'parts-actors/app/libs/parts-sources.jar')
    if os.path.isdir('parts-mrefs'):
        print "\tUpdating parts-mrefs"
        if not os.path.exists('parts-mrefs/app/libs'):
            os.makedirs('parts-mrefs/app/libs')
        shutil.copy('parts-base/app/release/parts.jar', 'parts-mrefs/app/libs/parts.jar')
        shutil.copy('parts-base/app/release/parts-sources.jar', 'parts-mrefs/app/libs/parts-sources.jar')
        if not os.path.exists('parts-mrefs/min3d-debug'):
            os.makedirs('parts-mrefs/min3d-debug')
        shutil.copy('parts-base/min3d/build/outputs/aar/min3d-debug.aar', 'parts-mrefs/min3d-debug/min3d-debug.aar')
    if os.path.isdir('parts-props'):
        print "\tUpdating parts-props"
        if not os.path.exists('parts-props/app/libs'):
            os.makedirs('parts-props/app/libs')
        shutil.copy('parts-base/app/release/parts.jar', 'parts-props/app/libs/parts.jar')
        shutil.copy('parts-base/app/release/parts-sources.jar', 'parts-props/app/libs/parts-sources.jar')
    if os.path.isdir('parts-roles'):
        print "\tUpdating parts-roles"
        if not os.path.exists('parts-roles/app/libs'):
            os.makedirs('parts-roles/app/libs')
        shutil.copy('parts-base/app/release/parts.jar', 'parts-roles/app/libs/parts.jar')
        shutil.copy('parts-base/app/release/parts-sources.jar', 'parts-roles/app/libs/parts-sources.jar')
        if not os.path.exists('parts-roles/min3d-debug'):
            os.makedirs('parts-roles/min3d-debug')
        shutil.copy('parts-base/min3d/build/outputs/aar/min3d-debug.aar', 'parts-roles/min3d-debug/min3d-debug.aar')
    if os.path.isdir('parts-sets'):
        print "\tUpdating parts-sets"
        if not os.path.exists('parts-sets/app/libs'):
            os.makedirs('parts-sets/app/libs')
        shutil.copy('parts-base/app/release/parts.jar', 'parts-sets/app/libs/parts.jar')
        shutil.copy('parts-base/app/release/parts-sources.jar', 'parts-sets/app/libs/parts-sources.jar')
    if os.path.isdir('parts-stages'):
        print "\tUpdating parts-stages"
        if not os.path.exists('parts-stages/app/libs'):
            os.makedirs('parts-stages/app/libs')
        shutil.copy('parts-base/app/release/parts.jar', 'parts-stages/app/libs/parts.jar')
        shutil.copy('parts-base/app/release/parts-sources.jar', 'parts-stages/app/libs/parts-sources.jar')
    if os.path.isdir('titles-imagetest'):
        print "\tUpdating titles-imagetest"
        if not os.path.exists('titles-imagetest/app/libs'):
            os.makedirs('titles-imagetest/app/libs')
        shutil.copy('parts-base/app/release/parts.jar', 'titles-imagetest/app/libs/parts.jar')
        shutil.copy('parts-base/app/release/parts-sources.jar', 'titles-imagetest/app/libs/parts-sources.jar')
    if os.path.isdir('titles-modeltest'):
        print "\tUpdating titles-modeltest"
        if not os.path.exists('titles-modeltest/app/libs'):
            os.makedirs('titles-modeltest/app/libs')
        shutil.copy('parts-base/app/release/parts.jar', 'titles-modeltest/app/libs/parts.jar')
        shutil.copy('parts-base/app/release/parts-sources.jar', 'titles-modeltest/app/libs/parts-sources.jar')
        if not os.path.exists('titles-modeltest/min3d-debug'):
            os.makedirs('titles-modeltest/min3d-debug')
        shutil.copy('parts-base/min3d/build/outputs/aar/min3d-debug.aar', 'titles-modeltest/min3d-debug/min3d-debug.aar')
    if os.path.isdir('titles-hellocube'):
        print "\tUpdating titles-hellocube"
        if not os.path.exists('titles-hellocube/app/libs'):
            os.makedirs('titles-hellocube/app/libs')
        shutil.copy('parts-base/app/release/parts.jar', 'titles-hellocube/app/libs/parts.jar')
        shutil.copy('parts-base/app/release/parts-sources.jar', 'titles-hellocube/app/libs/parts-sources.jar')
        if not os.path.exists('titles-hellocube/min3d-debug'):
            os.makedirs('titles-hellocube/min3d-debug')
        shutil.copy('parts-base/min3d/build/outputs/aar/min3d-debug.aar', 'titles-hellocube/min3d-debug/min3d-debug.aar')
    if os.path.isdir('titles-cubetest'):
        print "\tUpdating titles-cubetest"
        if not os.path.exists('titles-cubetest/app/libs'):
            os.makedirs('titles-cubetest/app/libs')
        shutil.copy('parts-base/app/release/parts.jar', 'titles-cubetest/app/libs/parts.jar')
        shutil.copy('parts-base/app/release/parts-sources.jar', 'titles-cubetest/app/libs/parts-sources.jar')
        if not os.path.exists('titles-cubetest/min3d-debug'):
            os.makedirs('titles-cubetest/min3d-debug')
        shutil.copy('parts-base/min3d/build/outputs/aar/min3d-debug.aar', 'titles-cubetest/min3d-debug/min3d-debug.aar')
    if os.path.isdir('titles-movietest'):
        print "\tUpdating titles-movietest"
        if not os.path.exists('titles-movietest/app/libs'):
            os.makedirs('titles-movietest/app/libs')
        shutil.copy('parts-base/app/release/parts.jar', 'titles-movietest/app/libs/parts.jar')
        shutil.copy('parts-base/app/release/parts-sources.jar', 'titles-movietest/app/libs/parts-sources.jar')
    if os.path.isdir('test-min3d_01'):
        print "\tUpdating test-min3d_01"
        if not os.path.exists('test-min3d_01/min3d-debug'):
            os.makedirs('test-min3d_01/min3d-debug')
        shutil.copy('parts-base/min3d/build/outputs/aar/min3d-debug.aar', 'test-min3d_01/min3d-debug/min3d-debug.aar')
    if os.path.isdir('test-min3d_02'):
        print "\tUpdating test-min3d_02"
        if not os.path.exists('test-min3d_02/min3d-debug'):
            os.makedirs('test-min3d_02/min3d-debug')
        shutil.copy('parts-base/min3d/build/outputs/aar/min3d-debug.aar', 'test-min3d_02/min3d-debug/min3d-debug.aar')
    return

# Stage parts-mrefs project.
def stagePartsMrefs() :
    print "Staging parts-mrefs...";
    if os.path.isdir('parts-actors'):
        print "\tUpdating parts-actors"
        if not os.path.exists('parts-actors/app/libs'):
            os.makedirs('parts-actors/app/libs')
        shutil.copy('parts-mrefs/app/release/mrefs.jar', 'parts-actors/app/libs/mrefs.jar')
        shutil.copy('parts-mrefs/app/release/mrefs-sources.jar', 'parts-actors/app/libs/mrefs-sources.jar')
    if os.path.isdir('parts-roles'):
        print "\tUpdating parts-roles"
        if not os.path.exists('parts-roles/app/libs'):
            os.makedirs('parts-roles/app/libs')
        shutil.copy('parts-mrefs/app/release/mrefs.jar', 'parts-roles/app/libs/mrefs.jar')
        shutil.copy('parts-mrefs/app/release/mrefs-sources.jar', 'parts-roles/app/libs/mrefs-sources.jar')
    if os.path.isdir('titles-imagetest'):
        print "\tUpdating titles-imagetest"
        if not os.path.exists('titles-imagetest/app/libs'):
            os.makedirs('titles-imagetest/app/libs')
        shutil.copy('parts-mrefs/app/release/mrefs.jar', 'titles-imagetest/app/libs/mrefs.jar')
        shutil.copy('parts-mrefs/app/release/mrefs-sources.jar', 'titles-imagetest/app/libs/mrefs-sources.jar')
    if os.path.isdir('titles-modeltest'):
        print "\tUpdating titles-modeltest"
        if not os.path.exists('titles-modeltest/app/libs'):
            os.makedirs('titles-modeltest/app/libs')
        shutil.copy('parts-mrefs/app/release/mrefs.jar', 'titles-modeltest/app/libs/mrefs.jar')
        shutil.copy('parts-mrefs/app/release/mrefs-sources.jar', 'titles-modeltest/app/libs/mrefs-sources.jar')
    if os.path.isdir('titles-hellocube'):
        print "\tUpdating titles-hellocube"
        if not os.path.exists('titles-hellocube/app/libs'):
            os.makedirs('titles-hellocube/app/libs')
        shutil.copy('parts-mrefs/app/release/mrefs.jar', 'titles-hellocube/app/libs/mrefs.jar')
        shutil.copy('parts-mrefs/app/release/mrefs-sources.jar', 'titles-hellocube/app/libs/mrefs-sources.jar')
    if os.path.isdir('titles-cubetest'):
        print "\tUpdating titles-cubetest"
        if not os.path.exists('titles-cubetest/app/libs'):
            os.makedirs('titles-cubetest/app/libs')
        shutil.copy('parts-mrefs/app/release/mrefs.jar', 'titles-cubetest/app/libs/mrefs.jar')
        shutil.copy('parts-mrefs/app/release/mrefs-sources.jar', 'titles-cubetest/app/libs/mrefs-sources.jar')
    if os.path.isdir('titles-movietest'):
        print "\tUpdating titles-movietest"
        if not os.path.exists('titles-movietest/app/libs'):
            os.makedirs('titles-movietest/app/libs')
        shutil.copy('parts-mrefs/app/release/mrefs.jar', 'titles-movietest/app/libs/mrefs.jar')
        shutil.copy('parts-mrefs/app/release/mrefs-sources.jar', 'titles-movietest/app/libs/mrefs-sources.jar')
    return

# Stage parts-roles project.
def stagePartsRoles() :
    print "Staging parts-roles...";
    if os.path.isdir('parts-props'):
        print "\tUpdating parts-props"
        if not os.path.exists('parts-props/app/libs'):
            os.makedirs('parts-props/app/libs')
        shutil.copy('parts-roles/app/release/roles.jar', 'parts-props/app/libs/roles.jar')
        shutil.copy('parts-roles/app/release/roles-sources.jar', 'parts-props/app/libs/roles-sources.jar')
    if os.path.isdir('parts-sets'):
        print "\tUpdating parts-sets"
        if not os.path.exists('parts-sets/app/libs'):
            os.makedirs('parts-sets/app/libs')
        shutil.copy('parts-roles/app/release/roles.jar', 'parts-sets/app/libs/roles.jar')
        shutil.copy('parts-roles/app/release/roles-sources.jar', 'parts-sets/app/libs/roles-sources.jar')
    if os.path.isdir('titles-imagetest'):
        print "\tUpdating titles-imagetest"
        if not os.path.exists('titles-imagetest/app/libs'):
            os.makedirs('titles-imagetest/app/libs')
        shutil.copy('parts-roles/app/release/roles.jar', 'titles-imagetest/app/libs/roles.jar')
        shutil.copy('parts-roles/app/release/roles-sources.jar', 'titles-imagetest/app/libs/roles-sources.jar')
    if os.path.isdir('titles-modeltest'):
        print "\tUpdating titles-modeltest"
        if not os.path.exists('titles-modeltest/app/libs'):
            os.makedirs('titles-modeltest/app/libs')
        shutil.copy('parts-roles/app/release/roles.jar', 'titles-modeltest/app/libs/roles.jar')
        shutil.copy('parts-roles/app/release/roles-sources.jar', 'titles-modeltest/app/libs/roles-sources.jar')
    if os.path.isdir('titles-hellocube'):
        print "\tUpdating titles-hellocube"
        if not os.path.exists('titles-hellocube/app/libs'):
            os.makedirs('titles-hellocube/app/libs')
        shutil.copy('parts-roles/app/release/roles.jar', 'titles-hellocube/app/libs/roles.jar')
        shutil.copy('parts-roles/app/release/roles-sources.jar', 'titles-hellocube/app/libs/roles-sources.jar')
    if os.path.isdir('titles-cubetest'):
        print "\tUpdating titles-cubetest"
        if not os.path.exists('titles-cubetest/app/libs'):
            os.makedirs('titles-cubetest/app/libs')
        shutil.copy('parts-roles/app/release/roles.jar', 'titles-cubetest/app/libs/roles.jar')
        shutil.copy('parts-roles/app/release/roles-sources.jar', 'titles-cubetest/app/libs/roles-sources.jar')
    if os.path.isdir('titles-movietest'):
        print "\tUpdating titles-movietest"
        if not os.path.exists('titles-movietest/app/libs'):
            os.makedirs('titles-movietest/app/libs')
        shutil.copy('parts-roles/app/release/roles.jar', 'titles-movietest/app/libs/roles.jar')
        shutil.copy('parts-roles/app/release/roles-sources.jar', 'titles-movietest/app/libs/roles-sources.jar')
    return

# Stage parts-props project.
def stagePartsProps() :
    print "Staging parts-props...";
    if os.path.isdir('parts-actors'):
        print "\tUpdating parts-actors"
        if not os.path.exists('parts-actors/app/libs'):
            os.makedirs('parts-actors/app/libs')
        shutil.copy('parts-props/app/release/props.jar', 'parts-actors/app/libs/props.jar')
        shutil.copy('parts-props/app/release/props-sources.jar', 'parts-actors/app/libs/props-sources.jar')
    if os.path.isdir('titles-imagetest'):
        print "\tUpdating titles-imagetest"
        if not os.path.exists('titles-imagetest/app/libs'):
            os.makedirs('titles-imagetest/app/libs')
        shutil.copy('parts-props/app/release/props.jar', 'titles-imagetest/app/libs/props.jar')
        shutil.copy('parts-props/app/release/props-sources.jar', 'titles-imagetest/app/libs/props-sources.jar')
    if os.path.isdir('titles-modeltest'):
        print "\tUpdating titles-modeltest"
        if not os.path.exists('titles-modeltest/app/libs'):
            os.makedirs('titles-modeltest/app/libs')
        shutil.copy('parts-props/app/release/props.jar', 'titles-modeltest/app/libs/props.jar')
        shutil.copy('parts-props/app/release/props-sources.jar', 'titles-modeltest/app/libs/props-sources.jar')
    if os.path.isdir('titles-hellocube'):
        print "\tUpdating titles-hellocube"
        if not os.path.exists('titles-hellocube/app/libs'):
            os.makedirs('titles-hellocube/app/libs')
        shutil.copy('parts-props/app/release/props.jar', 'titles-hellocube/app/libs/props.jar')
        shutil.copy('parts-props/app/release/props-sources.jar', 'titles-hellocube/app/libs/props-sources.jar')
    if os.path.isdir('titles-cubetest'):
        print "\tUpdating titles-cubetest"
        if not os.path.exists('titles-cubetest/app/libs'):
            os.makedirs('titles-cubetest/app/libs')
        shutil.copy('parts-props/app/release/props.jar', 'titles-cubetest/app/libs/props.jar')
        shutil.copy('parts-props/app/release/props-sources.jar', 'titles-cubetest/app/libs/props-sources.jar')
    if os.path.isdir('titles-movietest'):
        print "\tUpdating titles-movietest"
        if not os.path.exists('titles-movietest/app/libs'):
            os.makedirs('titles-movietest/app/libs')
        shutil.copy('parts-props/app/release/props.jar', 'titles-movietest/app/libs/props.jar')
        shutil.copy('parts-props/app/release/props-sources.jar', 'titles-movietest/app/libs/props-sources.jar')
    return

# Stage parts-stages project.
def stagePartsStages() :
    print "Staging parts-stages...";
    if os.path.isdir('parts-sets'):
        print "\tUpdating parts-sets"
        if not os.path.exists('parts-sets/app/libs'):
            os.makedirs('parts-sets/app/libs')
        shutil.copy('parts-stages/app/release/stages.jar', 'parts-sets/app/libs/stages.jar')
        shutil.copy('parts-stages/app/release/stages-sources.jar', 'parts-sets/app/libs/stages-sources.jar')
    if os.path.isdir('titles-imagetest'):
        print "\tUpdating titles-imagetest"
        if not os.path.exists('titles-imagetest/app/libs'):
            os.makedirs('titles-imagetest/app/libs')
        shutil.copy('parts-stages/app/release/stages.jar', 'titles-imagetest/app/libs/stages.jar')
        shutil.copy('parts-stages/app/release/stages-sources.jar', 'titles-imagetest/app/libs/stages-sources.jar')
    if os.path.isdir('titles-modeltest'):
        print "\tUpdating titles-modeltest"
        if not os.path.exists('titles-modeltest/app/libs'):
            os.makedirs('titles-modeltest/app/libs')
        shutil.copy('parts-stages/app/release/stages.jar', 'titles-modeltest/app/libs/stages.jar')
        shutil.copy('parts-stages/app/release/stages-sources.jar', 'titles-modeltest/app/libs/stages-sources.jar')
    if os.path.isdir('titles-hellocube'):
        print "\tUpdating titles-hellocube"
        if not os.path.exists('titles-hellocube/app/libs'):
            os.makedirs('titles-hellocube/app/libs')
        shutil.copy('parts-stages/app/release/stages.jar', 'titles-hellocube/app/libs/stages.jar')
        shutil.copy('parts-stages/app/release/stages-sources.jar', 'titles-hellocube/app/libs/stages-sources.jar')
    if os.path.isdir('titles-cubetest'):
        print "\tUpdating titles-cubetest"
        if not os.path.exists('titles-cubetest/app/libs'):
            os.makedirs('titles-cubetest/app/libs')
        shutil.copy('parts-stages/app/release/stages.jar', 'titles-cubetest/app/libs/stages.jar')
        shutil.copy('parts-stages/app/release/stages-sources.jar', 'titles-cubetest/app/libs/stages-sources.jar')
    if os.path.isdir('titles-movietest'):
        print "\tUpdating titles-movietest"
        if not os.path.exists('titles-movietest/app/libs'):
            os.makedirs('titles-movietest/app/libs')
        shutil.copy('parts-stages/app/release/stages.jar', 'titles-movietest/app/libs/stages.jar')
        shutil.copy('parts-stages/app/release/stages-sources.jar', 'titles-movietest/app/libs/stages-sources.jar')
    return

# Stage parts-sets project.
def stagePartsSets() :
    print "Staging parts-sets...";
    if os.path.isdir('titles-imagetest'):
        print "\tUpdating titles-imagetest"
        if not os.path.exists('titles-imagetest/app/libs'):
            os.makedirs('titles-imagetest/app/libs')
        shutil.copy('parts-sets/app/release/sets.jar', 'titles-imagetest/app/libs/sets.jar')
        shutil.copy('parts-sets/app/release/sets-sources.jar', 'titles-imagetest/app/libs/sets-sources.jar')
    if os.path.isdir('titles-modeltest'):
        print "\tUpdating titles-modeltest"
        if not os.path.exists('titles-modeltest/app/libs'):
            os.makedirs('titles-modeltest/app/libs')
        shutil.copy('parts-sets/app/release/sets.jar', 'titles-modeltest/app/libs/sets.jar')
        shutil.copy('parts-sets/app/release/sets-sources.jar', 'titles-modeltest/app/libs/sets-sources.jar')
    if os.path.isdir('titles-hellocube'):
        print "\tUpdating titles-hellocube"
        if not os.path.exists('titles-hellocube/app/libs'):
            os.makedirs('titles-hellocube/app/libs')
        shutil.copy('parts-sets/app/release/sets.jar', 'titles-hellocube/app/libs/sets.jar')
        shutil.copy('parts-sets/app/release/sets-sources.jar', 'titles-hellocube/app/libs/sets-sources.jar')
    if os.path.isdir('titles-cubetest'):
        print "\tUpdating titles-cubetest"
        if not os.path.exists('titles-cubetest/app/libs'):
            os.makedirs('titles-cubetest/app/libs')
        shutil.copy('parts-sets/app/release/sets.jar', 'titles-cubetest/app/libs/sets.jar')
        shutil.copy('parts-sets/app/release/sets-sources.jar', 'titles-cubetest/app/libs/sets-sources.jar')
    if os.path.isdir('titles-movietest'):
        print "\tUpdating titles-movietest"
        if not os.path.exists('titles-movietest/app/libs'):
            os.makedirs('titles-movietest/app/libs')
        shutil.copy('parts-sets/app/release/sets.jar', 'titles-movietest/app/libs/sets.jar')
        shutil.copy('parts-sets/app/release/sets-sources.jar', 'titles-movietest/app/libs/sets-sources.jar')
    return

# Stage parts-actors project.
def stagePartsActors() :
    print "Staging parts-actors...";
    if os.path.isdir('titles-imagetest'):
        print "\tUpdating titles-imagetest"
        if not os.path.exists('titles-imagetest/app/libs'):
            os.makedirs('titles-imagetest/app/libs')
        shutil.copy('parts-actors/app/release/actors.jar', 'titles-imagetest/app/libs/actors.jar')
        shutil.copy('parts-actors/app/release/actors-sources.jar', 'titles-imagetest/app/libs/actors-sources.jar')
    if os.path.isdir('titles-modeltest'):
        print "\tUpdating titles-modeltest"
        if not os.path.exists('titles-modeltest/app/libs'):
            os.makedirs('titles-modeltest/app/libs')
        shutil.copy('parts-actors/app/release/actors.jar', 'titles-modeltest/app/libs/actors.jar')
        shutil.copy('parts-actors/app/release/actors-sources.jar', 'titles-modeltest/app/libs/actors-sources.jar')
    if os.path.isdir('titles-hellocube'):
        print "\tUpdating titles-hellocube"
        if not os.path.exists('titles-hellocube/app/libs'):
            os.makedirs('titles-hellocube/app/libs')
        shutil.copy('parts-actors/app/release/actors.jar', 'titles-hellocube/app/libs/actors.jar')
        shutil.copy('parts-actors/app/release/actors-sources.jar', 'titles-hellocube/app/libs/actors-sources.jar')
    if os.path.isdir('titles-cubetest'):
        print "\tUpdating titles-cubetest"
        if not os.path.exists('titles-cubetest/app/libs'):
            os.makedirs('titles-cubetest/app/libs')
        shutil.copy('parts-actors/app/release/actors.jar', 'titles-cubetest/app/libs/actors.jar')
        shutil.copy('parts-actors/app/release/actors-sources.jar', 'titles-cubetest/app/libs/actors-sources.jar')
    if os.path.isdir('titles-movietest'):
        print "\tUpdating titles-movietest"
        if not os.path.exists('titles-movietest/app/libs'):
            os.makedirs('titles-movietest/app/libs')
        shutil.copy('parts-actors/app/release/actors.jar', 'titles-movietest/app/libs/actors.jar')
        shutil.copy('parts-actors/app/release/actors-sources.jar', 'titles-movietest/app/libs/actors-sources.jar')
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
