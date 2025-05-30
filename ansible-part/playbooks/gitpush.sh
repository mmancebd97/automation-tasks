#!/bin/bash


read -p "como quieres que se llame el push:" namepush

git add .
git commit -m "$namepush"
git push origin main
