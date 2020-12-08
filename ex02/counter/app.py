from flask import Flask, jsonify, request
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return jsonify({"Introduction": "Give me a vector and i'll count how many times its elements appear"})

@app.route('/count/', methods=['GET'])
def count():
	v = request.args.getlist('vector')
	print(v)

	bitmap = [['5', '0', '4', '10', '0', '7', '11', '12', '7', '2'],
	['7', '3', '7', '2', '4', '11', '12', '12', '11', '8'],
	['13', '8', '0', '4', '14', '2', '8', '7', '11', '1'],
	['12', '0', '2', '1', '11', '2', '9', '7', '15', '0'],
	['10', '6', '4', '2', '9', '8', '13', '6', '4', '8']]

	numbers = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']

	r = np.zeros(len(v), dtype=int)

	for i in range(len(bitmap)):
		for j in range(len(bitmap[i])):
			for k in range(len(v)):
				if (v[k] not in numbers):
					return jsonify({"Anwser": "Elements not in range"})
				if bitmap[i][j] == v[k]:
					r[k] = r[k] + 1
	aux = r.astype(str)
	asw = aux.tolist()
	return(dict(zip(v,asw)))