import random
import math
import re

from read_n_train import read, train, read_sentence


def unigram(files):
    tokens_h = list()
    tokens_m = list()
    for file in files:
        f = open("data/"+str(file)+".txt", "r")
        line = f.readline()
        temp = read(f, 1)
        if "HAMILTON" in line:          # for deciding hamilton, and creating hamilton unigram
            for i in range(len(temp)):
                tokens_h.append(temp[i])
        if "MADISON" in line:            # for deciding madison, and creating madison unigram
            for i in range(len(temp)):
                tokens_m.append(temp[i])
    hwordcount = len(tokens_h)          # count of all hamilton words
    mwordcount = len(tokens_m)           # count of all madison words
    unigramH = train(tokens_h)          # hamilton unigram model
    unigramM = train(tokens_m)          # madison unigram model
    return unigramH, unigramM, hwordcount, mwordcount


def prob_u(word, words_count, unig):        # without smoothing
    if word in unig:                            # this function for generated sentences.
        return unig[word] / words_count


def laplace_smoothing(word, words_count, unig):
    if word in unig:
        return math.log2((unig[word] + 1) / (words_count + len(unig)))
    else:
        return math.log2(1 / len(unig))


def generate_sentence_u(words_count, unig):
    cum = {}
    value = 0.0
    for word in unig:
        prb = prob_u(word, words_count, unig)
        cum[word] = value + prb                  # creating cumulative list
        value = value + prb
    sentence = ''
    for i in range(30):         # for 30 words
        rand = random.random()
        for word in cum:
            if rand <= cum[word]:
                if word != '</s>':              # if it is not '.' then go on
                    if i == 0:              # if it is first word of sentence
                        sentence = word
                    else:
                        sentence = sentence + ' ' + word       # add space between words
                    break
                else:                               # if it is a '.' then return and finish the sentence
                    sentence = sentence + ' ' + word
                    sentence = re.sub(' </s>', '.</s>', sentence)
                    return sentence

    return sentence


def prob_of_sentence_u(sentence, words_count, unig):    # it is used for prob of generated sentences or perplexity of essays
    tokens = read_sentence(sentence, 1)                         # returns the tokens of sentences
    prob = 0.0
    for word in tokens:
        prob = prob + laplace_smoothing(word, words_count, unig)

    return prob
