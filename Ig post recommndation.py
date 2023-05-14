import pandas as pd
import numpy as np
from sklearn.feature_extraction import text
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv("C:/Users/dell/Downloads/Datasets/Instagramdata.csv")
data.head()

data = data[["Caption", "Hashtags"]]
data.head()

captions = data["Caption"].tolist()
uni_tfidf = text.TfidfVectorizer(input = captions, stop_words = 'english')
uni_matrix = uni_tfidf.fit_transform(captions)
uni_sim = cosine_similarity(uni_matrix)

def recommend_post(x):
    return " | ".join(data["Caption"].loc[x.argsort()[-5:-1]])
data["Recommended Post"] = [recommend_post(x) for x in uni_sim]
data.head()

print(data["Recommended Post"][3])
