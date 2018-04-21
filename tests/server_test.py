import json
import requests
from pprint import pprint

baseUrl = 'http://localhost:8001/'

def test_only_primer3():
	task = json.load(open('test_only_primer3.json'))
	r = requests.post(baseUrl, data=json.dumps(task), headers={'content-type': 'application/json'})
	pprint(r.json())

if __name__ == '__main__':
	test_only_primer3()
