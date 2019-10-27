#usr/bin/env/python
# -*- coding: utf-8 -*-

import wxconv
from wxconv import WXC
import sys
fil = sys.argv[1]
fem_file=open(fil, 'r').read().splitlines()

data_file = fem_file
con = WXC(order='utf2wx')
data_transcripts = [row.decode('UTF-8') for row in data_file]

data_WX = [con.convert(row).encode('UTF-8') for row in data_transcripts]

#data_WX_words = [a + '\t' + b for a, b in zip(data_serial, data_WX)]
print data_WX
with open('./output_WX.txt', 'w') as outfile:
	 for wd in data_WX:
	     outfile.writelines(wd + '\n')
	 outfile.close()


### You would need to  manually remove word-final schwa, nukta in the output generated. ######
