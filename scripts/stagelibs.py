#!/usr/bin/python

# This script is used to stage the Magic Lantern Core and Parts libraries into their
# corresponding Android Studio projects.

import os
import shutil
import tempfile

print "Staging core-math...";
print "\tUpdating parts-roles"
if os.path.isdir('parts-roles'):
    shutil.copy('core-math/app/release/mlmath.jar', 'parts-roles/app/libs/mlmath.jar')
print "\tUpdating parts-sets"
if os.path.isdir('parts-sets'):
    shutil.copy('core-math/app/release/mlmath.jar', 'parts-sets/app/libs/mlmath.jar')
print "\tUpdating parts-stages"
if os.path.isdir('parts-stages'):
    shutil.copy('core-math/app/release/mlmath.jar', 'parts-stages/app/libs/mlmath.jar')
print "\tUpdating titles-imagetest"
if os.path.isdir('titles-imagetest'):
    shutil.copy('core-math/app/release/mlmath.jar', 'titles-imagetest/app/libs/mlmath.jar')

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

print "Staging parts-props...";
print "\tUpdating parts-props"
if os.path.isdir('parts-actors'):
    shutil.copy('parts-props/app/release/props.jar', 'parts-actors/app/libs/props.jar')
print "\tUpdating titles-imagetest"
if os.path.isdir('titles-imagetest'):
    shutil.copy('parts-props/app/release/props.jar', 'titles-imagetest/app/libs/props.jar')

print "Staging parts-stages...";
print "\tUpdating parts-staeges"
if os.path.isdir('parts-sets'):
    shutil.copy('parts-stages/app/release/stages.jar', 'parts-sets/app/libs/stages.jar')
print "\tUpdating titles-imagetest"
if os.path.isdir('titles-imagetest'):
    shutil.copy('parts-stages/app/release/stages.jar', 'titles-imagetest/app/libs/stages.jar')

print "Staging parts-sets...";
print "\tUpdating titles-imagetest"
if os.path.isdir('titles-imagetest'):
    shutil.copy('parts-sets/app/release/sets.jar', 'titles-imagetest/app/libs/sets.jar')

print "Staging parts-actors...";
print "\tUpdating titles-imagetest"
if os.path.isdir('titles-imagetest'):
    shutil.copy('parts-actors/app/release/actors.jar', 'titles-imagetest/app/libs/actors.jar')

print "...Done"
