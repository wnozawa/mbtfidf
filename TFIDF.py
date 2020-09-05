import sys
import MeCab
import numpy

def TFIDF_sims_argmax(doc, dictionary, tfidf, index):　
    m = MeCab.Tagger("-Owakati")
    stoplist = set('．,。,，,、,EOS,は,の,を,に,が,と,も,で,ば,し,て,う,た,ふ,これ,それ,あれ,この,その,あの,こと,する,ら,〔,〕,「,」,【,】,（,）,記号-空白,記号-括弧開,記号-括弧閉,for,a,of,the,and,to,in'.split(','))
    a = m.parse(doc.lower()).split()
    query_bow = dictionary.doc2bow([word for word in a if word not in stoplist])
    vec_tfidf = tfidf[query_bow]
    sims = index[vec_tfidf]

    # 類似度最大の文書インデックス
    sims_argmax=numpy.argmax(sims)

    return sims_argmax
