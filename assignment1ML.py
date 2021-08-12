#!/usr/bin/env python
# coding: utf-8

# In[5]:


s='Hi there class!'
arr=s.split(sep=' ')
print(arr)


# In[3]:


planet='Earth'
diameter=12742
print('The diameter of {} is {} kilometers' .format(planet,diameter))


# In[13]:


lst=[1,2,[3,4],[5,[100,200,['hello']],23,11],17]
print(lst[3][1][2][0])


# In[15]:


d={'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]['tricky'][3]['target'][3])


# In[8]:


def grab(s):
    ss=s.split('@')[-1]
    sss=ss.split('.')[-2]
    print(sss)
s='user@domain.com'
grab(s)
            


# In[4]:


#referred from gfg
def dog(dogg):
    if dogg.find('dog')==-1:
        return False
    else:
        return True
dog('hello mr dog how are you')
    
        
    


# In[9]:


def countdog(s):
    arr=s.split()
    n=0
    for i in arr:
        if i == 'dog':
            n=n+1
    print(n)
countdog('hello dog hey dog youre a good boi')


# In[11]:


#ref parth garg
seq = ['soup','dog','salad','cat','great']
list(filter(lambda word:word[0]!='s',seq))


# In[27]:


def speeding(speed,bday):
    if bday:
        speed=speed-5
    if speed<=60:
        print("no challan")
    elif speed>60 and speed<=80:
        print("small challan")
    elif speed>=81:
        print("heavy challan")
        

speeding(81,True)
speeding(81,False)


# In[18]:


arr1=['M','na','i','She']
arr2=['y','me','s','lly']
arr3=[]
for i in range(len(arr1)):
    arr3.append(arr1[i]+arr2[i])
print(arr3)


# In[19]:


arr1=['Hello ','take ']
arr2=['Dear ','Sir ']
arr3=[]
for i in range(len(arr1)):
    for j in range(len(arr2)):
        arr3.append(arr1[i]+arr2[j])
print(arr3)


# In[22]:


arr=[10,20,[300,400,[5000,6000],500],30,40]
arr[2][2].append(7000)
print(list1)


# In[24]:


arr=[23,28,87,2,20,1020]
for i in arr:
    if i==20:
        arr.remove(i)
print(arr)


# In[25]:


#ref parth garg
d1 = {'a': 100, 'b': 200, 'c': 300}
print(200 in d1.values())


# In[26]:


# ref gfg
import math
def serie(n):
    result=0.0246*(math.pow(10,n)-1-(9*n))
    return result
print(serie(3))


# In[ ]:




