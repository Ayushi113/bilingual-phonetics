import sys, string
ID_fil = open('../data/prompts_WX.txt').read().splitlines()
PBCM_II = open('../data/PBCM_WX_II.txt').read().splitlines()
PBCM_I = open('../data/PBCM_WX_I.txt').read().splitlines()

prompts = open('../data/PBCM2.txt').read().splitlines()
print prompts
#exit(0)
#print ID_fil
#exit(0)
print(len(ID_fil), len(prompts))
nlist = []
ID_fil = [kd.split('\t') for kd in ID_fil]
ID_fil = [[kd[0], kd[1].split(' ')] for kd in ID_fil]

vals = [' '.join(kd[1]) for kd in ID_fil]
vals2 = []
for pr in prompts:
	pr = pr.split(' ')
	pr = [w.replace('_', '') for w in pr]
	print pr
	vals2.append(' '.join(pr))
print len(vals2),len(vals)
dups = [val for val in vals if val not in vals2]
print len(dups), "dup", dups

for pr in prompts:
	pr = pr.split(' ')
	if pr[-1] == '.':
	   del pr[-1]
	tp = pr
	pr = [w.replace('_', '') for w in pr]# if w.startswith('_') and w.endswith('_') == True]
	for kd in ID_fil:
		if kd[1] == pr:
		   print "matches!\n\n"
		  # print kd[1], pr
		   kd[1] = tp
		   kd[1] = ' '.join(kd[1])
		   if kd not in nlist:
		   	nlist.append([kd[0], kd[1]])
		else:
			continue
			#print kd[1], pr
			#print '\n\n\n'
			
print(nlist[0:100])
with open('mod_data_check.txt', 'wb') as outfile:
	 for lin in nlist:
	 	 print lin
	 	 outfile.write('\t'.join(lin))
	 	 outfile.write('\n')
