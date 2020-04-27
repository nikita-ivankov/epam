from functools import wraps
from time import sleep

def delay(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		sleep(3)
		return func(*args, **kwargs)
	return wrapper