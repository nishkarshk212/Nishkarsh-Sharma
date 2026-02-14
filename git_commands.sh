#!/bin/bash
# Git commands script

echo "# MSG_DELETE_BOT" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/nishkarshk212/MSG_DELETE_BOT.git
git push -u origin main