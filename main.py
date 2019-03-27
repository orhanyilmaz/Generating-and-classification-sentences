from bigram import bigram
from unigram import unigram
from trigram import trigram
from gen_sentences import generate
from classification import classification

train_files = ["1", "6", "7", "8", "10", "13", "14", "15",  # Since there are no distinguishable details,
               "16", "17", "21", "22", "23", "24", "25",  # the files to be read are entered here.
               "26", "27", "28", "29", "37", "38", "39",
               "40", "41", "42", "43", "44", "45", "46"]

test_files = ["9", "11", "12", "47", "48", "49", "50",  # same here
              "51", "52", "53", "54", "55", "56", "57",
              "58", "62", "63"]

# if you want to see results on secreen, throw away the comment lines.

# print("task1")
# hamilton_uni, madison_uni, hwordcount, mwordcount = unigram(train_files)  # creating all n-gram models
# hamilton_bi, madison_bi = bigram(train_files)
# hamilton_t, madison_t = trigram(train_files)
#
# print("task2")
# generate(hamilton_uni, madison_uni, hamilton_bi,    # I have created a func that prints sentences on the screen
#          madison_bi, hamilton_t, madison_t, hwordcount, mwordcount)     # as there are no details in the paper sheet.
#
# print("task3")
# classification(test_files, hamilton_uni, madison_uni, hamilton_bi, madison_bi, hamilton_t, madison_t)
