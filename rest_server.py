#!/usr/bin/env

"""
	Author: Takao Shibamoto
	Date: 9/18/2017
	Description: REST server with only POST 
"""

import json, os
from flask import Flask, jsonify, abort, request, make_response, url_for, send_file, send_from_directory, Response
from primer3_utilities import *
from flask_cors import CORS
from rest_server_utility import *

# Flask app
app = Flask(__name__, static_url_path = "")
CORS(app)

# create cache folder if it doesnt exist yet
if not os.path.exists("cache"):
    os.makedirs("cache")

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


@app.route('/result/<string:task_id>', methods = ['GET'])
def get_result(task_id):
	""" Handle GET request to get a specific result
		Calculate the primer and return it
	Args:
		param1: Task ID
	Returns:
		JSON of the result
	"""

	inputPath = 'cache/'+task_id+'_input.json'
	resultPath = 'cache/'+task_id+'_result.json'

	try: # result file exists
		# load result data and return it
		resultFile = open(resultPath, 'r') 
		
	except IOError as e: # result file does not exist
		try: # input file exists
			findPrimersFromFile(inputPath, resultPath, 'better')
		except Exception as e: # input file does not exist
			abort(404)
		else: 
			resultFile = open(resultPath, 'r')
			result = json.load(resultFile)
			return jsonify(result)

	else: # no exception
		try:
			result = json.load(resultFile)
		except Exception as e:
			raise Exception('result file is broken')
		else:
			return jsonify(result)


@app.route('/', methods = ['POST'])
def add_task():
	""" Handle POST request to add an new primer3 task
	Returns:
		Url of the result
	"""

	requestedTask = request.json

	# make a new task ID
	task_id = idGenerator()

	inputPath = 'cache/'+task_id+'_input.json'

	try:
		inputData = requestedTask['input_data']
	except KeyError as e: # input_data doesn't exist
		return jsonify( { 'status':'error', 'error_statement': 'task JSON doesn\'t have input_data field'} ), 400

	# save input data as json file
	with open(inputPath, 'w') as outfile:
		json.dump(requestedTask['input_data'], outfile)

	print("New task (ID:{}) added".format(task_id))

	# return the URL of the result
	return jsonify( { 'status': 'ok', 'result_url': url_for('get_result', task_id = task_id, _external = True) } ), 201


if __name__ == '__main__':
	app.run(debug = True, port=5000)
	#app.run(host='0.0.0.0', port='5000')

