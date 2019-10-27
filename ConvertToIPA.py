# -*- coding: UTF-8 -*-
import epitran
from epitran.backoff import Backoff
from nltk.util import ngrams
import collections
from collections import Counter

epi = epitran.Epitran('hin-Deva')
s = 'हिन्दी'
slist = epi.trans_list(s)
	
def get_trigrams(token):
	n_grams = ngrams(token, 3)
	n_grams = [gram for gram in n_grams]
	return n_grams

def convertTuple(tup): 
    str =  ''.join(tup) 
    return str

hfile = open('/home/ayushi/Projects_2019/codemixed_analysis/parallel_devnWX_withID.txt').read().splitlines()
ipa_all = []
for i in hfile:
	sent = i.split('\t\t')
	hinsent = sent[2].split('\s')
	ipa = [get_trigrams(epi.trans_list(word)) for word in hinsent]
	ipa_all.append(ipa)

flat_list = [item for sublist in ipa_all for item in sublist]
flat_list = [item for sublist in flat_list for item in sublist]
counts = collections.Counter(flat_list)
print(counts)
