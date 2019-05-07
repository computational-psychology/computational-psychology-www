#!/bin/bash

make html
make publish

ghp-import output -b gh-pages

git push origin gh-pages
