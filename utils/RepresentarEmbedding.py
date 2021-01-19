import numpy as np
import nltk

class RepresentarEmbedding:

    def __init__(self, data):
        self._data = data

    def __call__(self, E):
        """
        Procesa los datos y obtiene los embeddings de los documentos (mediante la media).

        :param E: matriz de embeddings
        :return: representación mediante embeddings de los documentos
        """
        or_emb = []
        dim = len(E['and'])
        for response in self._data:
            sum = np.zeros((dim,))
            cont = 0
            for word in response:
                # Word embedding
                try:
                    sum += np.asarray(E[word])
                    cont += 1
                except Exception as l:
                    try:
                        stem_word = nltk.PorterStemmer().stem(word)
                        sum += np.asarray(E[stem_word])
                        cont +=1
                    except Exception as e:
                        pass
            or_emb.append((sum/cont).tolist())
        return or_emb
