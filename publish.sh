#!/bin/bash

git add content

git commit -a -m "changes at biancas computer"
git pull --rebase
git push

make publish


cp -R output/* /afs/tu-berlin.de/units/Fak_IV/psyco/www/www.psyco/htdocs/

