# Data models that power the API
from .data_structures import AttributeDict
from api import API


class Autor(AttributeDict):
	def __init__(self, name: str, type: str, api: API):
		self.name = name
		self.type = type
		self.__api = api

	def __repr__(self):
		return f"<Autor '{self.name}'>"


class Proposta(AttributeDict):
	def __init__(self, autor: Autor, ementa: str, ano: str, numero: str, keywords: tuple, api: API):
		self.autor = autor
		self.ementa = ementa
		self.ano = ano
		self.numero = numero
		self.keywords = keywords
		self`.__api = api

	def __repr__(self):
		return f"<Proposta '{self.numero}/{self.ano}'>"
