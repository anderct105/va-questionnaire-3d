import numpy as np

class CargarEmbedding:

    def __init__(self, path):
        self.path = path

    def loadGloveModel(self):
        """
        Carga modelo glove a partir de txt.

        :return: diccionario palabra : vector(float)
        """
        print("Loading Glove Model...")
        f = open(self.path, 'r')
        gloveModel = {}
        for line in f:
            splitLines = line.split(' ')
            word = splitLines[0]
            wordEmbedding = np.array([float(value) for value in splitLines[1:]])
            gloveModel[word] = wordEmbedding
        print(len(gloveModel), " words loaded!")
        return gloveModel