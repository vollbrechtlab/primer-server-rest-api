#!/usr/bin/env

"""
	Author: Takao Shibamoto
	Date: 9/18/2017
	Description: Rest server with only POST 
"""

from flask import Flask, jsonify, abort, request, make_response, url_for, send_file, send_from_directory, Response
import datetime
import time
from primer3_utilities import *
from flask_cors import CORS
import json


# Flask app
app = Flask(__name__, static_url_path = "")
CORS(app)


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
	return "Welcome to our primer3 rest API"


@app.route('/result/<string:task_id>', methods = ['GET'])
def get_result(task_id):
	""" Handle GET request to get a specific result
	Args:
		param1: Task ID
	Returns:
		JSON of the result
	"""

	# Get json data from database
	result = dbManager.getP3Result(task_id)

	if(result['status'] == 'does not exist'):
		abort(404)

	if(result['status'] == 'ok'):
		# read the parameters followed by "?"
		params = dict(request.args)
		if 'format' in params:
			if params['format'] == ['csv']:
				# return the response of the CSV file
				return createCsvRes('result_data/', '{}.csv'.format(task_id), result['result'])

			if params['format'] == ['raw']:
				print('a')
				return jsonify(result)

	return jsonify(createBetterP3Result(result))


@app.route('/', methods = ['POST'])
def add_task():
	""" Handle POST request to add an new primer3 task
	Returns:
		Successful: {'status': 'ok','result_url': 'url where result will be reported'} 
		Failed: {'status': 'error','error': 'error explanation'} 
	"""

	requestedTask = request.json

	# make a new task ID
	task_id = datetime.datetime.now().isoformat()

	# save input data as json file
	with open('input_data/'+task_id+'.json', 'w') as outfile:
		json.dump(requestedTask.input_data, outfile)

	print("New task (ID:{}) added".format(task_id))

	# return the URL of the result
	return jsonify( { 'result_url': url_for('get_result', task_id = task_id, _external = True), 'status': 'ok' } ), 201

if __name__ == '__main__':
	app.run(debug = True, port=3043)
	#app.run(host='0.0.0.0', port='3043')

