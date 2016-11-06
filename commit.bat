git add .
set tmp=%date:~0,10% %time:~0,8%
git commit -m "%tmp%"
git push