import math
import random
import re

from read_n_train import read, train, read_sentence
from bigram import prob_b


# all functions same as unigram but more parameters


def trigram(files):
    tokens_h = list()
    tokens_m = list()
    for file in files:
        f = open("data/" + str(file) + ".txt", "r")
        line = f.readline()
        temp = read(f, 3)
        if "HAMILTON" in line:
            for i in range(len(temp)):
                tokens_h.append(temp[i])
        if "MADISON" in line:
            for i in range(len(temp)):
                tokens_m.append(temp[i])
    trigramH = train(tokens_h)
    trigramM = train(tokens_m)
    return trigramH, trigramM


def prob_t(word, big, tri):
    word1 = word.split(" ")
    previous = word1[0] + " " + word1[1]
    if word in tri:
        if previous in big:
            return tri[word] / big[previous]


def laplace_smoothing(word, big, tri):
    word1 = word.split(" ")
    previous = word1[0] + " " + word1[1]
    if word in tri:
        if previous in big:
            return math.log2((tri[word] + 1) / (big[previous] + len(big)))
    else:
        if previous in big:
            return math.log2(1 / (big[previous] + len(big)))
        else:
            return math.log2(1 / (len(big)))


def for_head_of_sentence(big, cum, unig):           # in head of sentence we have to do bigram prob
    value = 0.0
    sentence = '<s>'
    a = sentence.split(" ")
    for word in big:
        token = word.split(" ")
        if token[0] == a[len(a) - 1]:
            prb = prob_b(word, unig, big)           # in this line i called prob_b (bigram prob)
            cum[word] = value + prb
            value = value + prb
    rand = random.random()
    for word in cum:
        if rand <= cum[word]:
            token = word.split(" ")
            sentence = word
            a.append(token[1])
            cum.clear()
            break
    return sentence, a


def generate_sentence_t(unig, big, tri):
    cum = {}
    value = 0.0
    sentence, a = for_head_of_sentence(big, cum, unig)
    for i in range(28):
        for word in tri:
            token = word.split(" ")
            p = token[0] + " " + token[1]
            if p == a[len(a) - 2] + " " + a[len(a) - 1]:
                prb = prob_t(word, big, tri)
                cum[word] = value + prb
                value = value + prb
        rand = random.random()
        for word in cum:
            if rand <= cum[word]:
                token = word.split(" ")
                if token[1] != '</s>':
                    if i == 0:
                        sentence = word
                        a.append(token[2])
                        cum.clear()
                        value = 0.0
                    else:
                        sentence = sentence + ' ' + token[2]
                        a.append(token[2])
                        cum.clear()
                        value = 0.0
                    break
                else:
                    sentence = sentence + ' ' + token[1]
                    sentence = re.sub(' </s> </s>', '.</s>', sentence)
                    return sentence

    return sentence


def prob_of_sentence_t(sentence, big, tri):
    tokens = read_sentence(sentence, 3)
    prob = 1
    for i in range(len(tokens)):
        prob = prob + laplace_smoothing(tokens[i], big, tri)

    return prob, len(tokens)
