import sys
import MeCab
import numpy

def TFIDF_prediction(doc, dictionary, tfidf, index, text_corpus):
    m = MeCab.Tagger("-Owakati")
    stoplist = set('．,。,，,、,EOS,は,の,を,に,が,と,も,で,ば,し,て,う,た,ふ,これ,それ,あれ,この,その,あの,こと,する,ら,〔,〕,「,」,【,】,（,）,記号-空白,記号-括弧開,記号-括弧閉,for,a,of,the,and,to,in'.split(','))
    a = m.parse(doc.lower()).split()
    query_bow = dictionary.doc2bow([word for word in a if word not in stoplist])
    vec_tfidf = tfidf[query_bow]
    sims = index[vec_tfidf]
    # print(list(enumerate(sims)))

    # 類似度順に文書を並べ替えて表示
    sim_result = sorted(enumerate(sims), key=lambda item: -item[1])
    # for i, s in enumerate(sim_result):
    #     print(s[1], text_corpus[s[0]])

    # print(sims)
    # print(sim_result)
    # print(sim_result[0][0],text_corpus[sim_result[0][0]])
    similar_question = text_corpus[sim_result[0][0]]

    response = "「" + similar_question + "」みたいな質問でしょうか？ちょっとわからないです。"

    return response

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
