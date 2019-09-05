class log:
	def __init__(self, orders: list):
		self.orders = orders

	def record(self, order_id):
		self.orders.append(order_id)

	def get_id(self, i: int):
		if not isinstance(i, int):
			raise TypeError("must be integer")
		else:
			return self.orders[-i]


def f(a: float, l: int = 0):
	print("a: ", a)
	print("l: ", l)

f(5,[1,2])
