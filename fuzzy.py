import numpy as np
a=[np.random.randint(4) for i in range(2486)]
b=[np.random.randint(4) for i in range(2486)]
c=[np.random.randint(4) for i in range(2486)]
d=[np.random.randint(4) for i in range(2486)]
e=[np.random.randint(4) for i in range(2486)]
f=[np.random.randint(4) for i in range(2486)]
g=[np.random.randint(4) for i in range(2486)]
h=[np.random.randint(4) for i in range(2486)]
j=[np.random.randint(4) for i in range(2486)]
ks=[np.random.randint(4) for i in range(2486)]
l=[np.random.randint(4) for i in range(2486)]


import pandas as pd
mn=pd.DataFrame({'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g,'h':h,'j':j,'k':ks,'l':l})
mn

mn.to_csv('E:/datasets/csv/fuzzy_dataset.csv')  #this is my location of my data 

m=[]
for i in mn['a']:
    if i>=2:
        m.append(1)
    else:
        m.append(0)

        
        
m1=[]
for i in mn['b']:
    if i>=2:
        m1.append(1)
    else:
        m1.append(0)
        
m2=[]
for i in mn['c']:
    if i>=2:
        m2.append(1)
    else:
        m2.append(0)
m3=[]
for i in mn['d']:
    if i>=2:
        m3.append(1)
    else:
        m3.append(0)

m4=[]
for i in mn['e']:
    if i>=2:
        m4.append(1)
    else:
        m4.append(0)
m5=[]
for i in mn['f']:
    if i>=2:
        m5.append(1)
    else:
        m5.append(0)

m6=[]
for i in mn['g']:
    if i>=2:
        m6.append(1)
    else:
        m6.append(0)

m7=[]
for i in mn['h']:
    if i>=2:
        m7.append(1)
    else:
        m7.append(0)

m8=[]
for i in mn['j']:
    if i>=2:
        m8.append(1)
    else:
        m8.append(0)

m9=[]
for i in mn['k']:
    if i>=2:
        m9.append(1)
    else:
        m9.append(0)

m10=[]
for i in mn['l']:
    if i>=2:
        m10.append(1)
    else:
        m10.append(0)

mn1=pd.DataFrame({'a':m,'b':m1,'c':m2,'d':m3,'e':m4,'f':m5,'g':m6,'h':m7,'j':m8,'k':m9,'l':m10})
mn1

l=mn1.sum(axis=0)
k=mn1.append(l,ignore_index=True)
k['column']=k.sum(axis=1)
k
l=k.sort_values(by=[2486],axis=1,ascending=False)
l
kl=l.sort_values(by=['column'],axis=0,ascending=False)
kl
clm=kl.drop('column',axis=1)
clm
final=clm.drop(2486,axis=0)
final
cor=mn1.corr()
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
sns.heatmap(cor,annot=True,cmap='BuGn_r')
