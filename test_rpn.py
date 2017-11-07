import unittest

import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate('1 1 +')
		self.assertEqual(2, result)   
	def test_subtract(self):
		result = rpn.calculate('5 3 -')
		self.assertEqual(2, result) 
	def test_multi(self):
		result = rpn.calculate('5 4 *')
		self.assertEqual(20, result) 

	def test_divide(self):
		result = rpn.calculate('16 8 /')
		self.assertEqual(2, result) 
	def test_mod(self):
		result = rpn.calculate('14 6 %')
		self.assertEqual(2, result) 
	def test_exp(self):
		result = rpn.calculate('2 4 ^')
		self.assertEqual(16, result)
