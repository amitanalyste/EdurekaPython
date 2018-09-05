class Date:
	def __init__(self, year, month, day): #year-month-day
		self.year = year
		self.month = month
		self.day = day
		# print("init")

	@classmethod
	def dmy(cls, day, month, year): #day-month-year
		# print("dmy")
		cls.year = year
		cls.month = month
		cls.day = day
		#order of return should be same as init
		return cls(cls.year, cls.month, cls.day)

	@classmethod
	def mdy(cls, month, day, year): #month-day-year
		# print("mdy")
		cls.year = year
		cls.month = month
		cls.day = day
		#order of return should be same as init
		return cls(cls.year, cls.month, cls.day)

a=Date(2016, 12, 11)
print(a.year) #2016

b=Date.dmy(9, 10, 2015)
print(b.year) #2015

a=Date.mdy(7, 8, 2014)
print(a.year) #2014