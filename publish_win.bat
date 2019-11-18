:: !/bin/bash

:: make html
make publish

:: This code here when we had the page hosted in Github pages. Now it's not the case anymore
:: ghp-import output -b gh-pages
:: git push origin gh-pages

:: we now have the page hosted in the TU server, wherer we access the folder via AFS
:: AFS should be already configured. Follow instructions here:
::  https://www.campusmanagement.tu-berlin.de/menue/dienste/daten_server/andrew_file_system/

xcopy output Z:\www\www.psyco\htdocs /e

