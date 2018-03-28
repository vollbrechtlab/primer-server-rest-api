#!/usr/bin/env python

"""
A thread to find primers from task
"""

__author__ = "Takao Shibamoto"
__copyright__ = "Copyright 2017, Vollbrecht Lab"
__date__ = "3/27/2018"
__version__ = "1.02"


import threading, json, string, random, logging
import fakePrimerDAFT

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('task.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def worker(task, taskId):
    """thread worker function"""

    saveTask(task, taskId)
    print('new task added: ' + taskId)
    logger.info('new task added ' + taskId)
    
    result = {}
    result['status'] = 'in process'

    saveResult(result, taskId)

    result = fakePrimerDAFT.run(task)
    print('result made: ' + taskId)
    logger.info('result made: ' + taskId)

    saveResult(result, taskId)


def saveResult(result, taskId):
    resultPath = 'cache/'+taskId+'_result.json'
    # save the result to a file
    with open(resultPath, 'w') as resultFile:
        json.dump(result, resultFile, sort_keys = True, indent = 4, ensure_ascii = False)


def saveTask(task, taskId):
    """ Save a task to a file
    Args:
        newTask: new task name
        taskId: new task ID
    """

    taskPath = 'cache/'+taskId+'_task.json'

    # save input data as json file
    with open(taskPath, 'w') as taskFile:
        json.dump(task, taskFile)

    return taskId


def startTask(task, taskId):
	threads = []
	t = threading.Thread(target=worker, args=(task,taskId))
	threads.append(t)
	t.start()
