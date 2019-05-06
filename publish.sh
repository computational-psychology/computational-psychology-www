#!/bin/bash

make publish

ghp-import output -b gh-pages

git push origin gh-pages
