pelican ./content/ -o output/ -s publishconf.py

xcopy output Z:\ /y

git commit -a -m "changes in Biancas laptop"
git push

