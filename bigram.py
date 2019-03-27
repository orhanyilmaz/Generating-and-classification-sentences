import math
import random
import re

from read_n_train import read, train, read_sentence


# all functions same as unigram but more parameters


def bigram(files):
    tokens_h = list()
    tokens_m = list()
    for file in files:
        f = open("data/" + str(file) + ".txt", "r")
        line = f.readline()
        temp = read(f, 2)
        if "HAMILTON" in line:
            for i in range(len(temp)):
                tokens_h.append(temp[i])
        if "MADISON" in line:
            for i in range(len(temp)):
                tokens_m.append(temp[i])
    bigramH = train(tokens_h)
    bigramM = train(tokens_m)
    return bigramH, bigramM


def prob_b(word, unig, big):
    word1 = word.split(" ")
    previous = word1[0]
    if word in big:
        if previous in unig:
            return big[word] / unig[previous]


def laplace_smoothing(word, unig, big):
    word1 = word.split(" ")
    previous = word1[0]
    if word in big:
        if previous in unig:
            return math.log2((big[word] + 1) / (unig[previous] + len(unig)))
    else:
        if previous in unig:
            return math.log2(1 / (unig[previous] + len(unig)))
        else:
            return math.log2(1 / (len(unig)))


def generate_sentence_b(unig, big):
    cum = {}
    value = 0.0
    sentence = '<s>'
    a = sentence.split(" ")
    for i in range(29):
        for word in big:
            token = word.split(" ")
            if token[0] == a[len(a) - 1]:
                prb = prob_b(word, unig, big)
                cum[word] = value + prb
                value = value + prb
        rand = random.random()
        for word in cum:
            if rand <= cum[word]:
                token = word.split(" ")
                if token[1] != '</s>':
                    if i == 0:
                        sentence = word
                        a.append(token[1])
                        cum.clear()
                        value = 0.0
                    else:
                        sentence = sentence + ' ' + token[1]
                        a.append(token[1])
                        cum.clear()
                        value = 0.0
                    break
                else:
                    sentence = sentence + ' ' + token[1]
                    sentence = re.sub(' </s>', '.</s>', sentence)
                    return sentence

    return sentence


def prob_of_sentence_b(sentence, unig, big):
    tokens = read_sentence(sentence, 2)
    prob = 0.0
    for i in range(len(tokens)):
        prob = prob + laplace_smoothing(tokens[i], unig, big)

    return prob, len(tokens)
