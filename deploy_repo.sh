rm -R ../primer-server/rest-api
mkdir ../primer-server/rest-api
cp {.gitignore,README.md,pdaft.conf,requirements.txt,server.py,start_server.sh,stop_server.sh,supported_genomes.json,task_thread.py,utilities.py,version.py} ../primer-server/rest-api/
cp -R primerDAFT ../primer-server/rest-api/
