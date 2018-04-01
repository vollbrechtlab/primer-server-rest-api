from subprocess import call
from version import __version__

repoPath = '../primer-server/rest-api/'
cpPath = repoPath + 'v' + __version__ + '/'
print('copying files to {}'.format(cpPath))
filesToCp = ['version.py', 'server.py', 'task_thread.py', 'utilities.py', 'fakePrimerDAFT.py']

# copy files
call(['rm', '-R', cpPath[:-1]])
call(['mkdir', cpPath[:-1]])
call(['cp'] + filesToCp + [cpPath])

# make .gitignore
with open(cpPath+'.gitignore', 'w') as outfile:
	outfile.write('__pycache__/\nlogs/\ncache/\n')

# make symbolic link to venv
call(['ln', '-s', '../venv', 'venv'], cwd=cpPath)
