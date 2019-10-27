import sys, string
import sys, string
ID_file = '/home/ayushi/Projects_2019/codemixed_analysis/PBCM_WX_only.txt'

devanagari_prompts = '/home/ayushi/Projects_2019/codemixed_analysis/parallel_devn_WX.txt'

ID_WX = {}
WX_devn = {}
groups = []
with open(ID_file) as f:
     for line in f:
         (key, val) = line.split('\t')
         ID_WX[key] = val

with open(devanagari_prompts) as f2:
     for line2 in f2:
      #   print(line2)
         (key2, val2) = line2.split('\t')
         WX_devn[key2] = val2
#print(ID_WX)
#print(WX_devn)

for key1, val1, in ID_WX.items():
    for key2, val2 in WX_devn.items():
        if ID_WX[key1][:-1] == key2[:-2]:
           tup = key1 + '\t\t' + val1[:-1] + '\t\t' + val2[:-1] 
           groups.append(tup)


with open('parallel_devnWX_withID.txt', 'w') as outfile:
	 for lin in groups:
	 	 print(lin)
	 	 outfile.write(lin)
	 	 outfile.write('\n')

           


