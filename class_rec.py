class Recurso(object):
	def __init__(self):
		self.__recursos = ['r0', 'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9']
		self.__req_usados = []

	def __getRecurso__(self):
		return self.__recursos

	def __getReq_usados__(self):
		return self.__req_usados

	def __alocaRecurso__(self, indice):
		x = self.__recursos[indice]
		del(self.__recursos[indice])
		self.__req_usados.append(x)

	def __desalocaRecurso__(self, indice):
		x = self.__req_usados[indice]
		del(self.__req_usados[indice])
		self.__recursos.append(x)

	def __alocaTodos__(self):
		for i in self.__recursos:
			self.__req_usados.append(i)

		self.__recursos.clear()

	def __desalocaTodos__(self):
		for i in self.__req_usados:
			self.__recursos.append(i)

		self.__req_usados.clear()