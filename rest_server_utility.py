import json, random, datetime, time, string

def idGenerator(size=16, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))