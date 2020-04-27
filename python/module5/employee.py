class Employee():
	def __init__(self, first_name, last_name, salary):
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.email = f"{first_name}_{last_name}@example.com".lower()
		self.salary = int(salary)

	@classmethod
	def from_str(cls, init_string):
		return cls(*init_string.split(","))

	@property
	def full_name(self):
		return f"{self.first_name}, {self.last_name}"

	@full_name.setter
	def full_name(self, name_string):
		self.first_name, self.last_name = name_string.title().replace(" ", "").split(",")


class DevOps(Employee):
	def __init__(self, first_name, last_name, salary, skills=[]):
		super().__init__(first_name, last_name, salary)
		self.skills = [skill.lower().title() for skill in skills]

	def add_skill(self, skill):
		if skill.lower().title() not in self.skills: self.skills.append(skill.lower().title())

	def remove_skill(self, skill):
		if skill.lower().title() in self.skills: self.skills.remove(skill.lower().title())


class Manager(Employee):
	def __init__(self, first_name, last_name, salary, subordinates=[]):
		super().__init__(first_name, last_name, salary)
		self.subordinates = subordinates

	def add_subordinate(self, DevOps):
		self.subordinates.append(DevOps)

	def remove_subordinate(self, for_remove):
		if isinstance(for_remove, DevOps) and for_remove in self.subordinates: 
			self.subordinates.remove(for_remove)
		else:
			for subordinate in self.subordinates:
				if subordinate.email == for_remove: self.subordinates.remove(subordinate)