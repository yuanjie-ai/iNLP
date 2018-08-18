from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer


class KerasBow(object):
    """doc
    词袋模型：我们可以为数据集中的所有单词制作一张词表，然后将每个单词和一个唯一的索引关联。
    每个句子都是由一串数字组成，这串数字是词表中的独立单词对应的个数。
    通过列表中的索引，我们可以统计出句子中某个单词出现的次数。
    """

    def __init__(self, num_words=20000, maxlen=None):
        """
        :param maxlen: 句子序列最大长度
        :param num_words: top num_words-1(词频降序)：保留最常见的num_words-1词
        """
        self.maxlen = maxlen
        self.num_words = num_words
        self.tokenizer = None

    def fit(self, docs):
        """
        :param corpus: ['some thing to do', 'some thing to drink']与sklearn提取文本特征一致
        """
        print('Create Bag Of Words ...')
        self.tokenizer = Tokenizer(self.num_words, lower=False) # 不改变大小写（需提前预处理）
        self.tokenizer.fit_on_texts(docs)
        print("Get Unique Words In Corpus: %s" % len(self.tokenizer.word_index))
        return self
        # self.tokenizer.word_index
        # self.tokenizer.word_counts

    def transform(self, docs):
        print('Docs To Sequences ...')
        sequences = self.tokenizer.texts_to_sequences(docs)
        pad_docs = pad_sequences(sequences, self.maxlen, padding='post')
        if self.maxlen is None:
            self.maxlen = pad_docs.shape[1]
        return pad_docs

    def fit_transform(self, docs):
        self.fit(docs)
        return self.transform(docs)
