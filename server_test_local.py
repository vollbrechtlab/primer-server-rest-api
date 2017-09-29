import json
import requests
from pprint import pprint

def test_bad_task():
	url = 'http://localhost:5000'
	task = {
		'task_info': {
			'email':'test1@example.com'
		},
		'input': {
			'SEQUENCE_TEMPLATE': 'ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA'
		}
	}

	r = requests.post(url, data=json.dumps(task), headers={'content-type': 'application/json'})
	pprint(r.json())

def test_bad_input_data():
	url = 'http://localhost:5000'
	task = {
		'task_info': {
			'email':'test1@example.com'
		},
		'input_data': {
			'SEQUENCE_TEMPLATE': 'ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA'
		}
	}

	r = requests.post(url, data=json.dumps(task), headers={'content-type': 'application/json'})
	pprint(r.json())

def test_bad_input_data2():
	url = 'http://localhost:5000'
	task = {
		'task_info': {
			'email':'test1@example.com'
		},
		'input_data': {
			'SEQUENCafasdfaE': 'ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA'
		}
	}

	r = requests.post(url, data=json.dumps(task), headers={'content-type': 'application/json'})
	pprint(r.json())

def test_ok():
	url = 'http://localhost:5000'
	task = {
		'format':'better',
		'input_data': {
			'SEQUENCE_ID': 'example',
			'SEQUENCE_TEMPLATE': 'ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA',
			'SEQUENCE_TARGET': (37,21),
			'SEQUENCE_INTERNAL_EXCLUDED_REGION': (37,21),
			'PRIMER_TASK': 'generic',
			'PRIMER_PICK_LEFT_PRIMER': True,
			'PRIMER_PICK_RIGHT_PRIMER': True,
			'PRIMER_OPT_SIZE': 18,
			'PRIMER_MIN_SIZE': 15,
			'PRIMER_MAX_SIZE': 21,
			'PRIMER_MAX_NS_ACCEPTED': 1,
			'PRIMER_PRODUCT_SIZE_RANGE': (75,100),
			'PRIMER_EXPLAIN_FLAG': True
		}
	}

	r = requests.post(url, data=json.dumps(task), headers={'content-type': 'application/json'})
	pprint(r.json())

def test_ok_bigdata():
	url = 'http://localhost:5000'
	testSqFile = open('test_seq.txt', 'r')
	task = {
		'format':'better',
		'input_data': {
			'SEQUENCE_TEMPLATE': testSqFile.read(),
			'PRIMER_PRODUCT_SIZE_RANGE': [ [ 165200, 495601 ] ]
		}
	}

	r = requests.post(url, data=json.dumps(task), headers={'content-type': 'application/json'})
	pprint(r.json())	

def test_ok_bigdata_raw():
	url = 'http://localhost:5000'
	testSqFile = open('test_seq.txt', 'r')
	task = {
		'input_data': {
			'SEQUENCE_TEMPLATE': testSqFile.read()
		}
	}

	r = requests.post(url, data=json.dumps(task), headers={'content-type': 'application/json'})
	pprint(r.json())	

if __name__ == '__main__':
	test_ok_bigdata_raw()
