#!/bin/bash

make publish

rsync -a --dry-run output/ guillermo.aguilar@sshgate.tu-berlin.de:/afs/tu-berlin.de/units/Fak_IV/psyco/www/www.psyco/htdocs
