def my_decorator(func):
	def test():
		print("Before function calls")
		func()
		print("After functionl calls")
	return test;

def square_number(func):
    def wrapper(num):
        result = func(num)
        return result * result
    return wrapper

@square_number
def get_number(x):
    return x

print( get_number(4))



@my_decorator
def hello():
	print("Hello")


hello()