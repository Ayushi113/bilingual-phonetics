filname = '/home/ayushi/Projects_2018/codemixed_ASR/modifications_2018/scripts/mod_data.txt'
fil = open(filname).read().splitlines()

fil = [lin.split('\t') for lin in fil]
fil_sents = [lin[1] for lin in fil]
fil_sents = [lin.split(' ') for lin in fil_sents]

wd_Eng = []
for lin in fil_sents:
	for wd in lin:
		if wd.startswith('_') and wd.endswith('_') == True:
			wd_Eng.append(wd)


with open('EngWords.txt', 'wb') as outfile:
	 for lin in wd_Eng:
	 	 print lin
	 	 outfile.write(lin.translate(None, '_'))
	 	 outfile.write('\n')


			


