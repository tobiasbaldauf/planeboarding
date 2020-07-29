#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Person:
    def __init__(self,id,row,seat):
            self.id = id
            self.row = row
            self.seat = seat
            self.wait=0
            self.waitingforseat=False
            
            
    def reducewait(self):
        if (self.wait>0):
            self.wait-=1
            
class Occu:
    def __init__(self,wait):
            self.wait=wait
            
            
    def reducewait(self):
        if (self.wait>0):
            self.wait-=1


# In[2]:


nrow=30;
nseat=6;

movewait=2
getinwait0=8
getinwait1=16
getinwait2=24

print nrow*nseat

p=[]
cnt=0
for i in range(nrow):
    for j in range(nseat):
        p.append(Person(cnt,i,nseat-j-1))
        cnt+=1
        


# In[3]:


for i in range(nrow):
    p.insert(0,0)
    
sb=[]
for i in range(len(p)):
    ss=[]
    for j in range(nseat):
        ss.append(0)
    sb.append(ss)
    
import random
#random.shuffle(p)
for i in range(40):
    if (p[i]!=0):
        print p[i].row,p[i].seat


# In[4]:



def printocc():
    occ=[]
    for i in range(nrow):
        if (p[i]==0):
            occ.append('e')
        else:
            occ.append(p[i].id)
    print occ

def checkempty():
    for i in range(len(p)):
        if (p[i]!=0):
            return False

    
    return True
    
printocc()
checkempty()


# In[5]:


def move():
    i=0
    while(i<len(p)):
        if (p[i]!=0):
            if (p[i].wait>0):
                #print 'wait'
                p[i].wait-=1
            if (p[i].wait==0 and i>0 and p[i].row<i and p[i-1]==0):
                p[i-1]=p[i]
                p[i]=0
                if (i<nrow and p[i+1]!=0):
                    p[i+1].wait=movewait
            elif (p[i].wait==0 and p[i].row==i):
                #print p[i].seat
                sb[i][p[i].seat]=p[i].id
                if (p[i+1]!=0):
                    p[i+1].wait+=getinwait0
                if (p[i].seat==2):
                    if (sb[i][0]!=0):
                        if (p[i+1]!=0):
                            p[i+1].wait+=getinwait1
                if (p[i].seat==3):
                    if (sb[i][1]!=0):
                        if (p[i+1]!=0):
                            p[i+1].wait+=getinwait1
                if (p[i].seat==4):
                    if (sb[i][0]!=0 and sb[i][2]!=0):
                        if (p[i+1]!=0):
                            p[i+1].wait+=getinwait2
                    elif (sb[i][0]!=0 or sb[i][2]!=0):
                        if (p[i+1]!=0):
                            p[i+1].wait+=getinwait1
                if (p[i].seat==5):
                    if (sb[i][1]!=0 and sb[i][3]!=0):
                        if (p[i+1]!=0):
                            p[i+1].wait+=getinwait2
                    elif (sb[i][1]!=0 or sb[i][3]!=0):
                        if (p[i+1]!=0):
                            p[i+1].wait+=getinwait1


                p[i]=0
            
        i+=1



# In[6]:


def move2():
    i=0
    while(i<len(p)):
        if (p[i]!=0):
            if (p[i].wait>0):
                #print 'wait'
                p[i].wait-=1
            if (p[i].wait==0 and i>0 and p[i].row<i and p[i-1]==0):
                p[i-1]=p[i]
                p[i]=0
                if (i<nrow and p[i+1]!=0):
                    p[i+1].wait=movewait
            elif (p[i].wait==0 and p[i].row==i):
                p[i].wait+=getinwait0
                if (p[i].seat==2):
                    if (sb[i][0]!=0):
                        p[i].wait+=getinwait1
                if (p[i].seat==3):
                    if (sb[i][1]!=0):
                        p[i].wait+=getinwait1
                if (p[i].seat==4):
                    if (sb[i][0]!=0 and sb[i][2]!=0):
                        p[i].wait+=getinwait2
                    elif (sb[i][0]!=0 or sb[i][2]!=0):
                        p[i].wait+=getinwait1
                if (p[i].seat==5):
                    if (sb[i][1]!=0 and sb[i][3]!=0):
                        p[i].wait+=getinwait2
                    elif (sb[i][1]!=0 or sb[i][3]!=0):
                        p[i].wait+=getinwait1
            elif (p[i].wait==1 and p[i].row==i):
                #print p[i].seat
                sb[i][p[i].seat]=p[i].id
                p[i]=0
            
        i+=1


# In[7]:


sb[0][0]


# In[8]:


import numpy as np
import matplotlib.pyplot as plt
a=np.zeros((220,nseat+1,nrow))
a[:,3]=-5

def fillmat(a):
    for i in range(nrow):
        if (p[i]!=0):
            a[3,i]=-1
        if (p[i]==0):
            a[3,i]=-5
        if (sb[i][0]!=0):
            a[2,i]=1
        if (sb[i][1]!=0):
            a[4,i]=1
        if (sb[i][2]!=0):
            a[1,i]=1
        if (sb[i][3]!=0):
            a[5,i]=1
        if (sb[i][4]!=0):
            a[0,i]=1
        if (sb[i][5]!=0):
            a[6,i]=1
        

for i in range(220):
    if (checkempty()):
        print 'done',i
        break
    fillmat(a[i])
    move2()
    #printocc()


# In[16]:


ax=plt.axes()
plt.pcolor(a[200],vmin=-5,vmax=1)
ax.set_xticks([])
ax.set_yticks([])


# In[17]:


print a[200][0,5]


# In[10]:


import matplotlib.animation as animation

fig = plt.figure()
ax=plt.axes()
i=0
ax.set_xticks([])
ax.set_yticks([])
im = plt.imshow(a[0],vmin=-5,vmax=1, animated=True)
def updatefig(*args):
    global i
    if (i<220):
        i += 1
    else:
        i=0
    im.set_array(a[i])
    return im,
ani = animation.FuncAnimation(fig, updatefig,  blit=True)

ani.save('test.mp4')
plt.show()


# In[ ]:




