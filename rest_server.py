#!/usr/bin/env

"""
	Author: Takao Shibamoto
	Date: 9/18/2017
	Description: REST server with only POST 
"""

import json, os, random, string
from flask import Flask, jsonify, abort, request, make_response, url_for, send_file, send_from_directory, Response
from flask_cors import CORS

from primer3_utilities import *


# Flask app
app = Flask(__name__, static_url_path = "")
CORS(app)

# create cache folder if it doesnt exist yet
if not os.path.exists("cache"):
    os.makedirs("cache")

def idGenerator(size=16, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

""" Error Handling """

@app.errorhandler(400)
def not_found(error):
	""" handle 400 error
	"""
	return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
	""" handle 404 error
	"""
	return make_response(jsonify( { 'error': 'Not found' } ), 404)


""" Route handling """
	
@app.route('/', methods = ['GET'])
def welcome():
	""" Say welcome
	"""
	return "Welcome to our primer3 REST API"


@app.route('/result/<string:taskId>', methods = ['GET'])
def get_result(taskId):
	""" Handle GET request to get a specific result
		Calculate the primer and return it
	Args:
		param1: Task ID
	Returns:
		JSON of the task result
	"""

	try: # result file exists in cache already
		# load result data and return it
		taskResultFile = openTaskResultFile(taskId)
		
	except Exception as e: # task result file does not exist
		try: # task file exists
			findPrimersFile(taskId)
		except Exception as e: # input file does not exist
			abort(404)

	# now task result file exists
	taskResultFile = openTaskResultFile(taskId)

	try: # load the task result from file
		taskResult = json.load(taskResultFile)
	except Exception as e:
		return jsonify( { 'status':'error', 'error_statement': 'task result is broken'} ), 400
	
	return jsonify(taskResult)


@app.route('/', methods = ['POST'])
def add_task():
	""" Handle POST request to add an new primer3 task
	Returns:
		URL of the task result url
	"""

	newTask = request.json

	# input_data key doesn't exist
	if not 'input_data' in newTask:
		return jsonify( { 'status':'error', 'error_statement': 'task doesn\'t have input_data field'} ), 400

	# SEQUENCE_TEMPLATE key doesn't exist
	if not 'SEQUENCE_TEMPLATE' in newTask['input_data']:
		return jsonify( { 'status':'error', 'error_statement': 'task[\"input_data\"] JSON doesn\'t have SEQUENCE_TEMPLATE field'} ), 400

	# make a new task ID
	taskId = idGenerator()

	saveTask(newTask, taskId)

	# return the URL of the result
	return jsonify( { 'status': 'ok', 'result_url': url_for('get_result', taskId = taskId, _external = True) } ), 201


if __name__ == '__main__':
	app.run(debug = True, port=5000)
	#app.run(host='0.0.0.0', port='5000')

