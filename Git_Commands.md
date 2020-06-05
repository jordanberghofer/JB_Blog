# Git Commands Reference for Shnooze
## -on master
git pull origin master\

## -create new branch
git branch *newBranchName*\
git switch *newBranchName*\
git push origin *newBranchName*\

## -now on the new branch
make changes\
git add "*"\
git commit -m "test commit message goes here"\
OR\
git commit\
"i" to insert text inside VIM\
Enter your message\
"Esc" : w q "enter"
git push origin *newBranchName*\

## -go to the website, resolve conflicts, and then merge to master

## -Switch to local master
git switch master\
git pull origin master\
git branch -D *newBranchName*\