import re
from bigram import prob_of_sentence_b
from trigram import prob_of_sentence_t
import math


def classification(files, hamilton_uni, madison_uni, hamilton_bi, madison_bi,  hamilton_t, madison_t):
    for file in files:
        print()
        f = open("data/" + str(file) + ".txt", "r")
        line = f.readline()                 # skip first line(hamilton, madison or unknown)
        line = f.readline()

        line = "<s> " + line
        s = line.lower()
        s = re.sub(r'[^a-zA-Z0-9\\.\\,\\<\\>\s]', '', s)    # cleaning all punct
        s = re.sub(r'[\\.]', ' </s> <s> ', s)
        s = re.sub('</s> <s> \n', '</s>', s)
        sentence = re.sub(r'[\\,]', ' ,', s)

        prb, n = prob_of_sentence_b(sentence, hamilton_uni, hamilton_bi)        # for hamilton_bigram perp
        value = prb * (-1 / n)                                                  # take prob * -1 / n
        perplexity_h_b = math.pow(2, value)                                     # take 2^value

        prb, n = prob_of_sentence_b(sentence, madison_uni, madison_bi)       # for madison_bigram perp
        value = prb * (-1 / n)
        perplexity_m_b = math.pow(2, value)

        if perplexity_h_b < perplexity_m_b:                             # if perp small it means prob high
            print("perplexity of hamilton = " + str(perplexity_h_b))
            print("perplexity of madison = " + str(perplexity_m_b))
            print(str(f.name) + " is a Hamilton's essay for bigram")

        else:
            print("perplexity of hamilton = " + str(perplexity_h_b))
            print("perplexity of madison = " + str(perplexity_m_b))
            print(str(f.name) + " is a Madison's essay for bigram ")

        prb, n = prob_of_sentence_t(sentence, hamilton_bi, hamilton_t)       # for hamilton_trigram perp
        value = prb * (-1 / n)
        perplexity_h_t = math.pow(2, value)

        prb, n = prob_of_sentence_t(sentence, madison_bi, madison_t)    # for madison_trigram perp
        value = prb * (-1 / n)
        perplexity_m_t = math.pow(2, value)

        if perplexity_h_t < perplexity_m_t:                             # same here
            print("perplexity of hamilton = " + str(perplexity_h_t))
            print("perplexity of madison = " + str(perplexity_m_t))
            print(str(f.name) + " is a Hamilton's essay for trigram")
        else:
            print("perplexity of hamilton = " + str(perplexity_h_t))
            print("perplexity of madison = " + str(perplexity_m_t))
            print(str(f.name) + " is a Madison's essay for trigram ")



