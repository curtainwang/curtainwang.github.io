deploy:
    jekyll build
    git add -A
    git commit -m "update source"
    echo "push source"
	git push