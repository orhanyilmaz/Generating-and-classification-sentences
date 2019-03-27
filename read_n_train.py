import re


def read(f, n):             # reads files, and tokenize them for unigram,bigram or trigram
    line = f.readline()         # it decides the model with parameter n
    while line:                         # n=1 for uni, n=2 for bi, n=3 for tri
        line = "<s> " + line
        s = line.lower()
        s = re.sub(r'[^a-zA-Z0-9\\.\\,\\<\\>\s]', '', s)             # cleaning all punct
        s = re.sub(r'[\\.]', ' </s> <s> ', s)
        s = re.sub('</s> <s> \n', '</s>', s)
        s = re.sub(r'[\\,]', ' , ', s)
        tokens = [token for token in s.split(' ') if token != ""]
        n_grams = zip(*[tokens[i:] for i in range(n)])      # for n=1 'to', for n=2 'to the', for n=3 'to the people'
        line = f.readline()

    return [" ".join(n_gram) for n_gram in n_grams]


def read_sentence(sentence, n):     # same as read but no need adding '<s>' or cleaning punct process
    tokens = [token for token in sentence.split(' ') if token != ""]
    n_grams = zip(*[tokens[i:] for i in range(n)])
    return [" ".join(n_gram) for n_gram in n_grams]


def train(tokens):          # creating models
    model = {}
    for i in range(len(tokens)):
        if tokens[i] in model:
            model[tokens[i]] = model[tokens[i]] + 1     # increase count of current word
        else:
            model[tokens[i]] = 1            # this word is new so count = 1
    return model
