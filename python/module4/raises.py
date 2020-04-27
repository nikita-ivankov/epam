def raises(exception):
	def decorator(func):
		def wrapper(*args, **kwargs):
			try:
				func(*args, **kwargs)
			except:
				raise exception
		return wrapper
	return decorator