#######################################################################################
#  In the name of God, the Compassionate, the Merciful
#  Pyabr (c) 2020 Mani Jamali. GNU General Public License v3.0
#
#  Official Website: 		http://pyabr.rf.gd
#  Programmer & Creator:    Mani Jamali <manijamali2003@gmail.com>
#  Gap channel: 			@pyabr
#  Gap group:   			@pyabr_community
#  Git source:              github.com/manijamali2003/pyabr
#
#######################################################################################

from buildlibs import pack_archives as pack
from buildlibs import control
import shutil, os, sys, hashlib,getpass

import shutil, os

## pre build ##

mode = input('choose your mode (stable,latest): ')

for i in os.listdir('packs'):
    pack.manifest(i)
shutil.rmtree('stor/tmp')
shutil.copytree('packs',f'stor/tmp')
f = open('stor/pack.sa','w')
f.write(f'''mkdir /tmp/all
mkdir /tmp/all/{mode}
paye pak /tmp/baran
mv /tmp/baran.pa /tmp/all/{mode}/baran.pa
paye pak /tmp/barge
mv /tmp/barge.pa /tmp/all/{mode}/barge.pa
paye pak /tmp/browser
mv /tmp/browser.pa /tmp/all/{mode}/browser.pa
paye pak /tmp/calculator
mv /tmp/calculator.pa /tmp/all/{mode}/calculator.pa
paye pak /tmp/calendar
mv /tmp/calendar.pa /tmp/all/{mode}/calendar.pa
paye pak /tmp/commento
mv /tmp/commento.pa /tmp/all/{mode}/commento.pa
paye pak /tmp/gap
mv /tmp/gap.pa /tmp/all/{mode}/gap.pa
paye pak /tmp/help
mv /tmp/help.pa /tmp/all/{mode}/help.pa
paye pak /tmp/stable
mv /tmp/stable.pa /tmp/all/stable.pa
paye pak /tmp/latest
mv /tmp/latest.pa /tmp/all/latest.pa
paye pak /tmp/lightword
mv /tmp/lightword.pa /tmp/all/{mode}/lightword.pa
paye pak /tmp/mines
mv /tmp/mines.pa /tmp/all/{mode}/mines.pa
paye pak /tmp/numix
mv /tmp/numix.pa /tmp/all/{mode}/numix.pa
paye pak /tmp/paint
mv /tmp/paint.pa /tmp/all/{mode}/paint.pa
paye pak /tmp/paye
mv /tmp/paye.pa /tmp/all/{mode}/paye.pa
paye pak /tmp/persia
mv /tmp/persia.pa /tmp/all/{mode}/persia.pa
paye pak /tmp/pyabr
mv /tmp/pyabr.pa /tmp/all/{mode}/pyabr.pa
paye pak /tmp/pyshell
mv /tmp/pyshell.pa /tmp/all/{mode}/pyshell.pa
paye pak /tmp/pysys
mv /tmp/pysys.pa /tmp/all/{mode}/pysys.pa
paye pak /tmp/roller
mv /tmp/roller.pa /tmp/all/{mode}/roller.pa
paye pak /tmp/runapp
mv /tmp/runapp.pa /tmp/all/{mode}/runapp.pa
paye pak /tmp/ubuntu-theme
mv /tmp/ubuntu-theme.pa /tmp/all/{mode}/ubuntu-theme.pa
paye pak /tmp/windows-theme
mv /tmp/windows-theme.pa /tmp/all/{mode}/windows-theme.pa
''')
f.close()

input('Are sure copy all package? press enter')
shutil.copytree('stor/tmp/all','repo')