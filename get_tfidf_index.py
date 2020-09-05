# load Q&A as dataframe
import pandas
df_qa = pandas.read_csv('AllQA.csv')

# get dataframe of Qs and convert it to list
df_q = df_qa.iloc[:,0]
q_corpus = df_q.astype(str).tolist()

# Morphological Analysis
import sys
import MeCab
m = MeCab.Tagger("-Owakati")
stoplist = set('．,。,，,、,EOS,は,の,を,に,が,と,も,で,ば,し,て,う,た,ふ,まで,これ,それ,あれ,この,その,あの,こと,する,ら,〔,〕,「,」,【,】,（,）,記号-空白,記号-括弧開,記号-括弧閉,for,a,of,the,and,to,in'.split(','))
a = [m.parse(document.lower()).split() for document in q_corpus]
texts = [[word for word in document if word not in stoplist] for document in a]

# count word appearance
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

# drop infrequent words
processed_corpus = [[token for token in text if frequency[token] > 1] for text in texts]

# get & save dictionary = list of words in processed_corpus with id
from gensim import corpora
dictionary = corpora.Dictionary(processed_corpus)

dictionary_name="maqa.dict"
dictionary.save(dictionary_name)

# get bag of words = list of (word id, word appearance) pairs
bow_corpus = [dictionary.doc2bow(text) for text in processed_corpus]

# get & save tfidf
from gensim import models
tfidf = models.TfidfModel(bow_corpus)
corpus_tfidf = tfidf[bow_corpus]

tfidf_name="tfidf.model"
tfidf.save(tfidf_name)

# get & save similarity index
from gensim import similarities
index = similarities.MatrixSimilarity(corpus_tfidf)
index_tfidf_name="index_tfidf.index"
index.save(index_tfidf_name)
