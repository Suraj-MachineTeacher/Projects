#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python

import sys

d = {}
for line in sys.stdin:
    k,f = line.split("\t")
    f = f[0:-1]                                                   # Removing /n from the filename 
    if k in d.keys():
        d[k].append(f)
    else:
        d[k] = [f]
for w in d.keys():
    d[w] = set(d[w])                                            #created a set for unique file names
    d[w] = list(d[w])                                           #created a list as required
    sys.stdout.write("{0}\t{1}\n".format(w,d[w]))               # Word and list of files.

