from matrix import count_in_matrix

def test_matriz():
	assert count_in_matrix([0, 7]) == '0=5\n7=6\n'

def test_matriz_5():
	assert count_in_matrix([5, 7]) == '5=0\n7=6\n'

def test_vector_zero():
	assert count_in_matrix([0]) == '0=5\n'

def test_vector_not_in_ranger():
	assert count_in_matrix([7,16, 0]) == 'Elements not in range'

def test_vector_null():
	assert count_in_matrix([]) == ''