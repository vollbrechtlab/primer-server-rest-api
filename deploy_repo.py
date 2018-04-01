from subprocess import call
from version import __version__
repoPath = '../primer-server/rest-api/'
cpPath = repoPath + 'v' + __version__ + '/'
print('copying files to {}'.format(cpPath))
filesToCp = ['version.py', 'server.py', 'task_thread.py', 'utilities.py', 'fakePrimerDAFT.py']

call(['rm', '-R', cpPath[:-1]])
call(['mkdir', cpPath[:-1]])
call(['cp'] + filesToCp + [cpPath])
