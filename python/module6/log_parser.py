import re
from collections import Counter 

class LogParser:
	def __init__(self, log_name):
		self.file = log_name

	def get_most_common(self, top):
		with open(self.file, 'r') as file:
			list_ip = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", file.read())
		
		return (Counter(list_ip).most_common(top))

	def log_by_http_code(self, output_file, code):
		with open(output_file, 'w') as destination:
			with open(self.file, 'r') as source:
				for line in re.findall(rf'.+HTTP\/\d.\d. {code} .+', source.read()):
					destination.write(line + '\n')