# http://www.slideshare.net/ogrisel/nltk-scikit-learnpyconfr2010ogrisel

import re
import math

def get_feature(sentence):
    return binary_occurrences(sentence)
    # return freq_unigram(sentence)
    # return tf_idf(sentence)

def binary_occurrences(sentence):
    words = re.split('[\w]+', sentence)
    word_set = set(words)
    feature = dict()
    for word in word_set:
        feature[word] = True

    return feature

def freq_unigram(sentence):
    words = re.split('[\w]+', sentence)
    word_set = set(words)
    l = len(words)

    feature = dict()
    for word in word_set:
        feature[word] = words.count(word) * 1.0 / l

    return feature

def tf_idf(sentence):
    words = re.split('[\w]+', sentence)

    word_set = set(words)
    l = len(words)

    tf = dict()
    for word in word_set:
        tf[word] = words.count(word) * 1.0 / l

    idf = dict()
    for word in word_set:
        idf[word] = math.log(tf[word])

    return idf