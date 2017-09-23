#!/usr/bin/env

"""
	Author: Takao Shibamoto
	Date: 9/30/2017
	Description: Excute primer3, format output
"""

from primer3.bindings import designPrimers
import json


def transformInput(data):
	""" separate input to seq_args and global_args
	Args: 
		param1: input data
	Returns:
		separated input data
	"""
	p3py_data = {}
	p3py_data['seq_args'] = {}
	p3py_data['global_args'] = {}
	for key in data.keys():
		if('SEQUENCE_' in key.upper()):
			p3py_data['seq_args'][key.upper()] = data[key]
		elif('PRIMER_' in key.upper()):
			p3py_data['global_args'][key.upper()] = data[key]

	return p3py_data


def createBetterResult(result):
	""" Create a primer3 result in a better format
	Args: 
		param1: primer3 result
	Returns:
		better result
	"""

	betterResult = {}

	for currIdx in range(result['PRIMER_PAIR_NUM_RETURNED']):
		betterResult['PRIMER_PAIR_{}'.format(currIdx)] = {}
		betterResult['PRIMER_PAIR_{}'.format(currIdx)]['COMPL_ANY_TH'] = result['PRIMER_PAIR_{}_COMPL_ANY_TH'.format(currIdx)]
		betterResult['PRIMER_PAIR_{}'.format(currIdx)]['COMPL_END_TH'] = result['PRIMER_PAIR_{}_COMPL_END_TH'.format(currIdx)]
		betterResult['PRIMER_PAIR_{}'.format(currIdx)]['PENALLTY'] = result['PRIMER_PAIR_{}_PENALTY'.format(currIdx)]
		betterResult['PRIMER_PAIR_{}'.format(currIdx)]['PRODUCT_SIZE'] = result['PRIMER_PAIR_{}_PRODUCT_SIZE'.format(currIdx)]
		betterResult['PRIMER_PAIR_{}'.format(currIdx)]['PRIMER_LEFT'] = {}
		betterResult['PRIMER_PAIR_{}'.format(currIdx)]['PRIMER_LEFT']['START'] = result['PRIMER_LEFT_{}'.format(currIdx)][0]
		betterResult['PRIMER_PAIR_{}'.format(currIdx)]['PRIMER_LEFT']['LENGTH'] = result['PRIMER_LEFT_{}'.format(currIdx)][1]
		betterResult['PRIMER_PAIR_{}'.format(currIdx)]['PRIMER_LEFT']['END_STABILITY'] = result['PRIMER_LEFT_{}_END_STABILITY'.format(currIdx)]
		betterResult['PRIMER_PAIR_{}'.format(currIdx)]['PRIMER_LEFT']['GC_PERCENT'] = result['PRIMER_LEFT_{}_GC_PERCENT'.format(currIdx)]
		betterResult['PRIMER_PAIR_{}'.format(currIdx)]['PRIMER_LEFT']['HAIRPIN_TH'] = result['PRIMER_LEFT_{}_HAIRPIN_TH'.format(currIdx)]
		betterResult['PRIMER_PAIR_{}'.format(currIdx)]['PRIMER_LEFT']['PENALTY'] = result['PRIMER_LEFT_{}_PENALTY'.format(currIdx)]
		betterResult['PRIMER_PAIR_{}'.format(currIdx)]['PRIMER_LEFT']['SELF_ANY_TH'] = result['PRIMER_LEFT_{}_SELF_ANY_TH'.format(currIdx)]
		betterResult['PRIMER_PAIR_{}'.format(currIdx)]['PRIMER_LEFT']['SELF_END_TH'] = result['PRIMER_LEFT_{}_SELF_END_TH'.format(currIdx)]
		betterResult['PRIMER_PAIR_{}'.format(currIdx)]['PRIMER_LEFT']['SEQUENCE'] = result['PRIMER_LEFT_{}_SEQUENCE'.format(currIdx)]
		betterResult['PRIMER_PAIR_{}'.format(currIdx)]['PRIMER_LEFT']['TM'] = result['PRIMER_LEFT_{}_TM'.format(currIdx)]
		betterResult['PRIMER_PAIR_{}'.format(currIdx)]['PRIMER_RIGHT'] = {}
		betterResult['PRIMER_PAIR_{}'.format(currIdx)]['PRIMER_RIGHT']['START'] = result['PRIMER_RIGHT_{}'.format(currIdx)][0]
		betterResult['PRIMER_PAIR_{}'.format(currIdx)]['PRIMER_RIGHT']['LENGTH'] = result['PRIMER_RIGHT_{}'.format(currIdx)][1]
		betterResult['PRIMER_PAIR_{}'.format(currIdx)]['PRIMER_RIGHT']['END_STABILITY'] = result['PRIMER_RIGHT_{}_END_STABILITY'.format(currIdx)]
		betterResult['PRIMER_PAIR_{}'.format(currIdx)]['PRIMER_RIGHT']['GC_PERCENT'] = result['PRIMER_RIGHT_{}_GC_PERCENT'.format(currIdx)]
		betterResult['PRIMER_PAIR_{}'.format(currIdx)]['PRIMER_RIGHT']['HAIRPIN_TH'] = result['PRIMER_RIGHT_{}_HAIRPIN_TH'.format(currIdx)]
		betterResult['PRIMER_PAIR_{}'.format(currIdx)]['PRIMER_RIGHT']['PENALTY'] = result['PRIMER_RIGHT_{}_PENALTY'.format(currIdx)]
		betterResult['PRIMER_PAIR_{}'.format(currIdx)]['PRIMER_RIGHT']['SELF_ANY_TH'] = result['PRIMER_RIGHT_{}_SELF_ANY_TH'.format(currIdx)]
		betterResult['PRIMER_PAIR_{}'.format(currIdx)]['PRIMER_RIGHT']['SELF_END_TH'] = result['PRIMER_RIGHT_{}_SELF_END_TH'.format(currIdx)]
		betterResult['PRIMER_PAIR_{}'.format(currIdx)]['PRIMER_RIGHT']['SEQUENCE'] = result['PRIMER_RIGHT_{}_SEQUENCE'.format(currIdx)]
		betterResult['PRIMER_PAIR_{}'.format(currIdx)]['PRIMER_RIGHT']['TM'] = result['PRIMER_RIGHT_{}_TM'.format(currIdx)]

	return betterResult


def findPrimers(inputData, resultFormat="better"):
	""" return primer3 result with given format
	Args: 
		param1: input data
		param2: result format (raw/better)
	Returns:
		result
	"""
	p3pyInputData = transformInput(inputData)

	result = {}
	try:
		result = designPrimers(p3pyInputData['seq_args'], p3pyInputData['global_args'])
	except: # input data is broken
		raise Exception('input data does not have correct parameters')

	if resultFormat == "better":
		return createBetterResult(result);

	return result


def findPrimersFromFile(inputPath, outputPath, resultFormat="better"):
	""" Create a primer3 result in a better format
	Args: 
		param1: input json location
		param2: output json location
		param3: result of task
	"""

	inputFile = None
	try: 
		inputFile = open(inputPath, 'r')
	except IOError as e:
		raise Exception("input file does not exist")

	inputData = None
	try: 
		inputData = json.load(inputFile)
	except:
		raise Exception('input JSON data is broken')

	taskResult = {}
	try:
		taskResult['result'] = findPrimers(inputData, resultFormat)
	except Exception as e:
		taskResult['status'] = 'error'
		taskResult['error_statement'] = str(e)
	else:
		taskResult['status'] = 'ok'

	# save the result to a file
	with open(outputPath, 'w') as outputFile:
		json.dump(taskResult, outputFile, sort_keys = True, indent = 4, ensure_ascii = False)

	
		
