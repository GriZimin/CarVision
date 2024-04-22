set /p x="Enter the name of the commit: "
git add *
git commit -m %x%
git push
pause