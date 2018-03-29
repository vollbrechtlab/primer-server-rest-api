git checkout dev
git add --all .
git commit -m "small change"
git push origin dev
rm -R /tmp/primer-server-rest-api-tmp
mkdir /tmp/primer-server-rest-api-tmp
rsync -aP . /tmp/primer-server-rest-api-tmp/ --exclude=.git --exclude=venv --exclude=updateRepo.sh
git checkout master
cp -a /tmp/primer-server-rest-api-tmp/. ./
git add --all .
git commit -m "from dev"
git push origin master
git checkout dev
