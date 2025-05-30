#!/bin/bash

rute=$(pwd)
read -p "como quieres que se llame el push:" $namepush

git add $rute .
git commit -m "$namepush"
git push origin main
