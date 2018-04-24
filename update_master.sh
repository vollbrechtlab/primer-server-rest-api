# make sure to push dev first
git checkout dev
git add --all .
git commit -m "small change"
git push origin dev

# cleanup current tmp
rm -fR /tmp/primer-server-rest-api-tmp
mkdir /tmp/primer-server-rest-api-tmp

# copy all nessesary files to /tmp/primer-server-rest-api-tmp/
cp {.gitignore,LICENSE,README.md,deploy_repo.py,pdaft.conf,requirements.txt,server.py,start_server.sh,stop_server.sh,supported_genomes.json,task_thread.py,utilities.py,version.py} /tmp/primer-server-rest-api-tmp/
cp -R primerDAFT /tmp/primer-server-rest-api-tmp/
cp -R tests /tmp/primer-server-rest-api-tmp/

# go to master branch
git checkout master
git pull

# remove nessasary files
rm .angular-cli.json .editorconfig .gitignore README.md deploy.js karma.conf.js package-lock.json package.json protractor.conf.js tsconfig.json tslint.json
rm -R src
rm -R e2e
rm -R other_data

# copy back all files in /tmp/primer-server-rest-api-tmp/ to master and push
cp -a /tmp/primer-server-rest-api-tmp/. ./
git add --all .
git commit -m "$1"
git push origin master

# come back to dev
git checkout dev
