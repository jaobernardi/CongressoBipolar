# Data models that power the API
from .data_structures import AttributeDict


class Autor(AttributeDict):
	def __init__(self, name, type):
		self.name = name
		self.type = type

	def __repr__(self):
		return f"<Autor '{self.name}'>"


class Proposta(AttributeDict):
	def __init__(self, autor, ementa, ano, numero, keywords):
		self.autor = autor
		self.ementa = ementa
		self.ano = ano
		self.numero = numero
		self.keywords = keywords

	def __repr__(self):
		return f"<Proposta '{self.numero}/{self.ano}'>"
