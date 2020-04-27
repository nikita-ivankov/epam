#Don't know when TypeError may occur(I mean in which operation), so I've decided to raise it manually

def multiple_in_range(begin, end):
	result = []
	if (type(begin) == int) and (type(end) == int):
		while (begin <= end):
			if (begin % 7 == 0) and (begin % 5 != 0):
				result.append(begin)
			begin += 1
		return result
	else:
		raise TypeError("Type error occur")
