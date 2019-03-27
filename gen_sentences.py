from bigram import generate_sentence_b, prob_of_sentence_b
from unigram import generate_sentence_u, prob_of_sentence_u
from trigram import generate_sentence_t, prob_of_sentence_t


def generate(hamilton_uni, madison_uni, hamilton_bi, madison_bi, hamilton_t, madison_t, hwordcount, mwordcount):

    for i in range(2):
        sentence_u_h = generate_sentence_u(hwordcount, hamilton_uni)    # generate sentence from hamilton unigram
        print("Hamilton Uni = " + str(sentence_u_h))
        prb_u_h = prob_of_sentence_u(sentence_u_h, hwordcount, hamilton_uni)    # take prob of sentence
        print("Probability = " + str(prb_u_h))
        print()

        sentence_u_m = generate_sentence_u(mwordcount, madison_uni)     # generate sentence from madison unigram
        print("Madison Uni = " + str(sentence_u_m))
        prb_u_m = prob_of_sentence_u(sentence_u_m, mwordcount, madison_uni)  # take prob of sentence
        print("Probability = " + str(prb_u_m))
        print()

    for i in range(2):
        sentence_b_h = generate_sentence_b(hamilton_uni, hamilton_bi)       # generate sentence from madison bigram
        print("Hamilton Bi = " + str(sentence_b_h))
        prb_b_h, n = prob_of_sentence_b(sentence_b_h, hamilton_uni, hamilton_bi)     # take prob of sentence
        print("Probability = " + str(prb_b_h))
        print()
        sentence_b_m = generate_sentence_b(madison_uni, madison_bi)     # generate sentence from madison bigram
        print("Madison Bi = " + str(sentence_b_m))
        prb_b_m, n = prob_of_sentence_b(sentence_b_m, madison_uni, madison_bi)   # take prob of sentence
        print("Probability = " + str(prb_b_m))
        print()
    for i in range(2):
        sentence_t_h = generate_sentence_t(hamilton_uni, hamilton_bi, hamilton_t)   # generate sentence from hamilton trigram
        print("Hamilton Tri = " + str(sentence_t_h))
        prb_t_h, n = prob_of_sentence_t(sentence_t_h, hamilton_bi, hamilton_t)   # take prob of sentence
        print("Probability = " + str(prb_t_h))
        print()
        sentence_t_m = generate_sentence_t(madison_uni, madison_bi, madison_t)      # generate sentence from madison trigram
        print("Madison Tri = " + str(sentence_t_m))
        prb_t_m, n = prob_of_sentence_t(sentence_t_m, madison_bi, madison_t)     # take prob of sentence
        print("Probability = " + str(prb_t_m))
        print()



