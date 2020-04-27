#don't know how to store file(data) - in class attribute or reopen file in any time class method starts, decided to use first one

class CsvParser:

	def __init__(self, file_name):
		self.file = file_name


	def sell_over(self, item_type: str, threshold: int):
		result = []
		with open(self.file) as data:
			reader = csv.DictReader(data)	

			for line in reader:
				if line['Item Type'] == item_type and int(line['Units Sold']) > threshold:
					result.append(line['Country']) 
		return sorted(result)


	def get_country_profit(self, country):
		result = 0.0
		with open(self.file) as data:
			reader = csv.DictReader(data)			
			for line in reader:
				if line['Country'] == country:
					result += float(line['Total Profit'])
		return float("{0:.2f}".format(result))


	def save_as(self, new_file_name, delimiter):
		with open(self.file) as data:
			with open(new_file_name, 'w') as copy_file:    
				reader = csv.DictReader(data)	

				column_names = ["Region","Country","Item Type","Sales Channel","Order Priority","Order Date",\
				"Order ID","Ship Date","Units Sold","Unit Price","Unit Cost","Total Revenue","Total Cost","Total Profit"] 

				cvs_writter = csv.DictWriter(copy_file, fieldnames=column_names, delimiter=delimiter)
				cvs_writter.writeheader()
				cvs_writter.writerows(reader)