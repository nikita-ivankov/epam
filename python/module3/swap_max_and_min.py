#Don't know why but double assignment doesn't work in this case, I tried differently

def swap_max_and_min(values):
	if len(set(values)) != len(values): 
		raise ValueError("Value error occur")
	else:
		#values[values.index(min(values))], values[values.index(max(values))] = max(values), min(values)
		#values[values.index(min(values))], values[values.index(max(values))]  = values[values.index(max(values))],values[values.index(min(values))]
		result = values.copy()
		result[values.index(min(values))] = max(values)
		result[values.index(max(values))] = min(values)
		return result

if __name__ == "__main__":
	print(swap_max_and_min([1,2,3]))