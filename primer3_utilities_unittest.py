import json, unittest
from primer3_utilities import *

"""
f = open('test_seq.txt', 'r')
print(f.read())


inputData = {
	
}
"""

def readJson(fileName):
	f = None
	try:
		f = open(fileName, 'r')
	except:
		print('error opening file')
		return None

	data = None
	try:
		data = json.load(f)
	except:
		print('error parsing json')
		return None

	return data

def printJson(data):
	print(json.dumps(data, sort_keys=True, indent=4))

testTask = readJson('test_task.json')
testResultRaw = readJson('test_result_raw.json')

#printJson(task)
#print(task["input_data"]["PRIMER_PICK_LEFT_PRIMER"])

class Primer3UtilitiesTest(unittest.TestCase):
	""" test for primer3 utilities """
	"""
	def testRaw(self):
		result = findPrimers(testTask["input_data"])
		self.assertEqual(result['PRIMER_LEFT_2_SEQUENCE'], "CCTGGAGGGTGGCCC")
	"""

	def testBetter(self):
		result = findPrimers(testTask["input_data"], testTask['format'])
		self.assertEqual(result['pairs'][2]['PRIMER_LEFT']['SEQUENCE'], 'CCTGGAGGGTGGCCC')
		self.assertEqual(result['pairs'][4]['PRIMER_LEFT']['SEQUENCE'], 'CCTGGAGGGTGGCCC')
		self.assertEqual(result['pairs'][0]['PRIMER_RIGHT']['SEQUENCE'], 'TCAAACCACCAAGCGAGGA')
		self.assertEqual(result['pairs'][0]['PRIMER_RIGHT']['SEQUENCE'], 'TCAAACCACCAAGCGAGGA')
	"""
	def testInternalOligoBetter(self):
		testTask["input_data"]["PRIMER_PICK_INTERNAL_OLIGO"] = True
		result = findPrimers(testTask["input_data"], testTask['format'])
		self.assertTrue(result['pairs'][0]['PRIMER_INTERNAL']['SEQUENCE'] is not None)
	"""
		
unittest.main()