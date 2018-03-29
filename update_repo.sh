# make sure to push dev first
git checkout dev
git add --all .
git commit -m "small change"
git push origin dev

# copy all dev except .git and venv to /tmp/primer-server-rest-api-tmp/
rm -R /tmp/primer-server-rest-api-tmp
mkdir /tmp/primer-server-rest-api-tmp
rsync -aP . /tmp/primer-server-rest-api-tmp/ --exclude=.git --exclude=venv --exclude=updateRepo.sh

# copy back all files in /tmp/primer-server-rest-api-tmp/ to master
git checkout master
cp -a /tmp/primer-server-rest-api-tmp/. ./
git add --all .
git commit -m "from dev"
git push origin master

# come back to dev
git checkout dev
