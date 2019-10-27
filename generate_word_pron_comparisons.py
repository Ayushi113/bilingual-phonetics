## Reading the two sources of pronunciation
epitran_wx = open('/home/ayushi/Projects_2019/codemixed_analysis/text_data/OutputWxEpitran.txt').read().splitlines()
espeak = open('/home/ayushi/Projects_2019/codemixed_analysis/text_data/OutputEspeak.txt').read().splitlines()
espeak = [e.split('\t') for e in espeak]
espeak_dic = {t[0]:t[1] for t in espeak}
## 
def convert_to_dic(lis):
	lis = [sent.split('\t\t')[1:] for sent in lis]
	#print(lis)
	#exit(0)
	lisp = []
	for ids in lis:
		case = [sent.split(' ') for sent in ids]
		lisp.append(case)
	#print(lisp)
	pronunciation, pronunciation_final = [], []
	for sent in lisp:
		for word in range(len(sent)):
			word, prons = sent[1][word], [sent[1][word], sent[0][word], sent[2][word]]
			pronunciation.append(prons) if prons not in pronunciation else pronunciation
#	print(len(set(pronunciation)))
#	exit(0)
	for word in pronunciation:
		for key in espeak_dic.keys():
			if word[0] == key:

			   word = word + [espeak_dic[key]]
			   print(word)
	#print(pronunciation)

convert_to_dic(epitran_wx)
#for word in espeak
