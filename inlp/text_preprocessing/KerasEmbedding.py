import numpy as np
from keras.layers import Embedding


class KerasEmbedding(object):
    def __init__(self, fname, maxlen, word_index):
        """
        :param fname: 词向量路径
        :param maxlen: 句序列最大长度
        :param word_index: KerasBow().tokenizer.word_index
        """
        self.fname = fname
        self.maxlen = maxlen
        self.word_index = word_index
        self.embeddings_index, self.embeddings_dim = self.gensim_load_wv()  # self.file_load_wv()

    def get_keras_embedding(self, train_embeddings=False):
        print('Get Keras Embedding Layer ...')
        # prepare embedding matrix
        num_words = len(self.word_index) + 1  # 未出现的词标记0
        embedding_matrix = np.zeros((num_words, self.embeddings_dim))
        # embedding_matrix = np.random.random((num_words, EMBEDDING_DIM))  # np.random.normal(size=(num_words, EMBEDDING_DIM))
        for word, idx in self.word_index.items():
            if word in self.embeddings_index:
                # words not found in embedding index will be all-zeros.
                embedding_matrix[idx] = self.embeddings_index[word]
        # note that we set trainable = False so as to keep the embeddings fixed
        embedding_layer = Embedding(input_dim=num_words,
                                    output_dim=self.embeddings_dim,
                                    weights=[embedding_matrix],
                                    input_length=self.maxlen,
                                    trainable=train_embeddings)
        return embedding_layer

    def gensim_load_wv(self):
        try:
            import gensim
            print('Load Word Vectors ...')
            model = gensim.models.KeyedVectors.load_word2vec_format(self.fname)
            return model, model.vector_size
        except ImportError:
            raise ImportError("Please install gensim")

    def file_load_wv(self):
        print('Load Word Vectors ...')
        embeddings_index = {}
        with open(self.fname) as f:
            for line in f:
                line = line.split()
                if len(line) > 2:
                    embeddings_index[line[0]] = np.asarray(line[1:], dtype='float32')
        return embeddings_index, len(line[1:])
