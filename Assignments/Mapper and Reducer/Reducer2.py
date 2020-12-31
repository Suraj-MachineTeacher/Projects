#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python

import sys

d = {}
for x in sys.stdin:
    k,f= x.split("\t")
    f = f[:-1]
    if k in d.keys():
       d[k].append(f)
        
    else:
        d[k] = [f]
for w in d.keys():
    u = {}
    for v in d[w]:
        u[v] = d[w].count(v)  #creating counter for dictionary. Could not use Counter as HDFS was preventing me to import counter 
                                                                                    
    sys.stdout.write("{0}\t{1}\n".format(w,u))

