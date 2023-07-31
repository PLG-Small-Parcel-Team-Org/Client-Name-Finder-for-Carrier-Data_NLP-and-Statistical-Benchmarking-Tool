import nltk
import pandas as pd
from nltk.metrics.distance import jaccard_distance
from nltk.util import ngrams

def jaccard_similarity(x,y):

    return 1 - jaccard_distance(x,y)

def get_similarity_by_n_grams(left, right, n):
    seq1 = set(nltk.word_tokenize(left, n=n))
    seq2 = set(nltk.word_tokenize(right, n=n))

    similarity = 1 - jaccard_distance(seq1, seq2)

input1 = ["P. Poll", "Petal & Cat", "Nuckerruck", "Princess Shiane"]
input2 = ["Polly P."]

rows = []

for client1 in input1:
    row = []

    for client2 in input2:
        sequence1 = set(client1)
        sequence2 = set(client2)

        row.append(client1)
        row.append(client2)
        row.append(jaccard_similarity(sequence1, sequence2))

        rows.append(row)

rows.sort(key = lambda row: row[2])
print(rows[-1])
