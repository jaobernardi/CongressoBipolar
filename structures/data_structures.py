# Data structures that power the API

class AttributeDict:
	def __setitem__(self, key, value):
		self.__setattr__(key.lower(), value)
	def __getitem__(self, key):
		return self.__getattribute__(key.lower())
