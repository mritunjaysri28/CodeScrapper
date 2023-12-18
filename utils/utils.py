import json

def read_json(file):
	try:
		with open(file=file,mode='r') as f:
			return json.load(fp=f)
	except FileNotFoundError:
	    print(f"File {file} not found.")