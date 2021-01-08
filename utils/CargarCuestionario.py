import pandas as pd


class CargarCuestionario:
	"""
	Carga las preguntas de una hoja de cálculo .xls.

	Attributes
	----------
	path : str
		Path al archivo con las preguntas.
	hoja : str
		Hoja del archivo de cálculo del que se van a coger las preguntas.
	columna : str
		Nombre de las columnas de las que se van a coger los datos.
	"""

	def __init__(self, path, hoja=None, columna=None):
		self.path = path
		self.hoja = hoja
		self.columna = columna

	def cargar_excel(self):
		"""
		Obtiene los enunciados de las preguntas del archivo xls del cuestionario.
		https://docs.google.com/document/d/12CuJU7WmJjteB2hro7BsqDEHKIP7YMz1bijjq91nEnQ/edit#heading=h.h9kii3g0aw5b
		Returns
		-------
		list of str
			La lista de enunciados.
					"""
		df = pd.ExcelFile(self.path).parse(self.hoja)
		return df[self.columna].tolist()

	def cargar_txt(self) -> list:
		"""
		Carga las preguntas de un archivo de texto en self.path en el que cada línea corresponde a una pregunta.

		Returns
		-------
		list of str
			Lista con los enunciados cargados del fichero.
		"""
		with open(self.path, 'r') as f:
			enunciados = f.read()
			f.close()
		return enunciados.split('\n')

	def __call__(self, formato='excel') -> list:
		"""
		Carga las preguntas desde un archivo en base al formato de archivo.

		Parameters
		----------
		formato : str
			Formato excel o txt.

		Returns
		-------
		list of str
			Lista de enunciados con las preguntas.
		"""
		if formato.__eq__('excel'):
			return self.cargar_excel()
		else:
			return self.cargar_txt()
