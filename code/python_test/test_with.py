class div:
	def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2
		self.res = num1 / num2


class test_with:

	def __init__(self, num1, num2):
		self.str = 'one test_with object'
		print('in init, create {}'.format(self.str))
		self.num1 = num1
		self.num2 = num2

	def __enter__(self):
		print('in entry')
		if self.num2 == 0:
			raise Exception
		div_obj = div(self.num1, self.num2)
		return div_obj

	def __exit__(self, exc_type, exc_value, exc_tb):
		print('in exit')
		if exc_tb is not None:
			print('type = {}value = {}traceback = {}'.format(exc_type, exc_value, exc_tb))
			print('Error!')
			return True
		else:
			print('Success!')



with test_with(2, 1) as div_obj:
	print('in with statment')
	print('{} / {} = {}'.format(
		div_obj.num1, div_obj.num2, div_obj.res))

with test_with(2, 1) as div_obj:
	print('in with statment')
	raise Exception
	print('{} / {} = {}'.format(
		div_obj.num1, div_obj.num2, div_obj.res))