import sys
import numpy as np
from itertools import combinations

DOC_ID=[]
WORDS=[]
for i, x in enumerate(sys.stdin):
    if i==0:
        N=int(x.split()[0])
    elif i%2==1:
        DOC_ID.append(x.split()[0])
    elif i%2==0:
        WORDS.append(x.split())

def solution(N, DOC_ID, WORDS):
    news_db={}
    distinct_words=[]
    for x, y in zip(DOC_ID, WORDS):
        news_db[x]=y
        distinct_words.extend(y)
    distinct_words=list(set(distinct_words))
    tf_idf=makeVectors(N, news_db, distinct_words)

    similarities=[]
    for i in range(N-1):
        for j in range(i+1, N):
            similarity=cosineSimilarity(tf_idf[DOC_ID[i]], tf_idf[DOC_ID[j]])
            similarities.append([DOC_ID[i], DOC_ID[j], similarity])
        similarities=[x for x in similarities if x[2]>=0.98]
        similarities.sort(key=lambda x: x[0], reverse=True)

    cluster=[]
    checked=[]
    for idx, doc in enumerate(DOC_ID):
        if doc in checked :
            continue
        cluster.append([doc])
        similarity=[x for x in similarities if doc in x]
        cluster[-1].extend([x[1] for x in similarity])
        checked.extend(cluster[-1])


    print(len(cluster))
    for i in range(len(cluster)):
        print(cluster[i][0], len(cluster[i]))


def makeVectors(N, news_db, distinct_words):
    tf={}
    max_td={}

    for key, words_li in news_db.items():
        temp=[]
        for word in distinct_words:
            temp.append(words_li.count(word))
        tf[key]=temp

    for i in range(len(distinct_words)):
        max_val=0
        cnt=0
        for key, val in tf.items():
            cnt+=val[i]
            if val[i]>max_val:
                max_val=val[i]
        max_td[distinct_words[i]]=[max_val, cnt]

    for key, li in tf.items():
        for i, word in enumerate(distinct_words):
            val=(0.5+0.5*(li[i]/max_td[word][0]))
            if val !=0:
                tf[key][i]=val*np.log(N/abs(max_td[word][1]))
            else:
                tf[key][i]=val*np.log(N/(1+abs(max_td[word][1])))

    return tf

def cosineSimilarity(vec1, vec2):
    dot_product=np.dot(vec1, vec2)
    l2_norm=(np.sqrt(sum(np.square(vec1)))*np.sqrt(sum(np.square(vec2))))

    return dot_product/l2_norm

if __name__=="__main__":
    solution(N, DOC_ID, WORDS)
