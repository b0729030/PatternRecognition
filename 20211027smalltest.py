#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sympy as sm
i, n= sm.symbols('i, n') 

for k in range(10): 

     

    f= sm.Sum( i**k,  

              (i, 1, n)) 

     

    結果= f.doit() 

     

    print(f'k= {k}') 

    print(f'f= {f}') 

    display(f) 

    display(結果) 

    print("-"*10) 


# In[ ]:




