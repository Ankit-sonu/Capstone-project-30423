class MyIterator:
	def __iter__(self):
		self.num = 1
		return self

	def __next__(self):
		if self.num <=10:
			result = self.num
			self.num += 2
			return result
		else:
			raise StopIteration

obj = MyIterator()
it = iter(obj)

for i in it:
	print(i)