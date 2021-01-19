import string
import nltk


class Preprocesar:

    def __init__(self, corpus):
        self.corpus = corpus

    def __call__(self, pad='<PAD>'):
        """
        Realiza el preproceso del texto para obtener vectores a partir de tokens
        a partir del texto, eliminando puntuación y palabras comunes del inglés.

        :param corpus: vector de textos
        :param pad: valor a utilizar para el padding, el cual se añade al vocabulario
        :return: un vector con palabras para cada texto y el vocabulario generado con el ínndice
        """
        nltk.download('punkt')
        corpus_prep = []
        vocab = []
        for response in self.corpus:
            response_tokenized = nltk.word_tokenize(response)
            response_prep = []
            # Eliminar puntuacion
            for word in response_tokenized:
                word = word.lower()
                if word not in string.punctuation:
                    response_prep.append(word)
                    vocab.append(word)
            corpus_prep.append(response_prep)
        vocab.append(pad)
        vocab = {x: index for index, x in enumerate(set(vocab))}
        return corpus_prep, vocab
