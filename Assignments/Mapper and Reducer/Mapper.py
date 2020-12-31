#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python

import sys
import os
import string                                                      #To remove punctuations.

l = ["a","e","i","o","u"]                                          #list to comapre vowels   
for line in sys.stdin:                                                
    c = line.lower()                                                  #Making every line a lower case
    c = ''.join(s for s in c if s not in string.punctuation)       #removing punctuations
    ws = c.strip().split()                                          #creating required words
    filepath = os.getenv("map_input_file")                         #getting the path of the file
    file = filepath.split("/")                                     #splitting file name by "/"
    filename = file[-1]                                            # last word is the file name
    for w in ws:                                                   #every word in a line
        if w[0] in l and len(w) > 6:                             #if word starts with vowel and if word is greater than 6 characters
           sys.stdout.write("{0}\t{1}\n".format(w,filename))      #print word and filename

