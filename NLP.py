# Import libraries
import nltk
import pandas as pd
from nltk.metrics.distance import jaccard_distance
from nltk.util import ngrams

# Create jaccard_similarity function to get jaccard_distance
def jaccard_similarity(x,y):

    return 1 - jaccard_distance(x,y)

# N-Grams Function
def get_similarity_by_n_grams(left, right, n):
    seq1 = set(nltk.word_tokenize(left, n=n))
    seq2 = set(nltk.word_tokenize(right, n=n))

    similarity = 1 - jaccard_distance(seq1, seq2)

# Create row function to find most similar client
def create_row(client1, client2, df, client_column_name):
    row = []
    sequence1 = set(client1)
    sequence2 = set(client2)

    row.append(client1)
    row.append(client2)
    row.append(jaccard_similarity(sequence1, sequence2))
    row.append(df[client_column_name].value_counts()[client1])

    return row

input1 = ["P. Poll", "Petal & Cat", "Nuckerruck", "Princess Shiane"]
input2 = ["Polly P."]

# Create final_rows list
final_rows = []

# For loop to iterate through list of clients
for client1 in input2:

# Create rows list
    rows = []

# Lambda function to collect every client's most compatible name
    rows = list(map(lambda client2: create_row(client1, client2, df), input1))

# Sort rows by jaccard_distance
    rows.sort(key = lambda row: row[2])
    
# Append final_rows with the Most compatible collection of data
    final_rows.append(rows[-1])
    final_rows.sort(key=lambda row: row[2])
