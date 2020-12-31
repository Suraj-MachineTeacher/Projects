#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Name: Suraj Suresh")


# In[ ]:


from urllib.request import urlopen


# In[ ]:


t = "Y"
while t == "Y":
    print("Insert Ticker")
    x = input()
    url = ("https://financialmodelingprep.com/api/v3/quote-short/{g}?apikey=4de707451f9485218f3370128a8059de".
           format(g = x.upper()))
    b = urlopen(url)
    data = b.read().decode("utf-8")
    print (data)
    print("Do you want to continue? Y/N")
    t = input()
    t = t.upper()
else:
    print("Lets look at Historical Daily Price with Change and Volume Interval")    


# In[ ]:


t = "Y"
while t == "Y":
    print("Insert Ticker")
    x = input()
    print("Start Date in YYYY-MM-DD format")
    st = input()
    print("End Date in YYYY-MM-DD format")
    e = input()
    url = ("https://financialmodelingprep.com/api/v3/historical-price-full/{g}?from={st}&to={e}&apikey=4de707451f9485218f3370128a8059de"
           .
           format(g = x.upper(),st=st,e=e))
    b   = urlopen(url)
    data = b.read().decode("utf-8")
    print (data)
    print("Do you want to continue? Y/N")
    t = input()
    t = t.upper()
print("Thank you for your time and patience!")

