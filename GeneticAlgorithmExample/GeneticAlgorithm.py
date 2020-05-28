# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt  
import random

get_bin = lambda x, n: format(x, 'b').zfill(n)

b_x = 7
b_y = 8

indiv = []

def fun(x,y):
    return pow(x,2) - (2*x*y)+pow(y,2)

def copy(a, begin, end):
    r = ""
    #for i in range(begin,end+1):
    i = begin
    while i != (end+1):
        r = r+a[i]
        i = i+1
    return r

def decimal(b):
    n = 0
    for i in range(0,len(b)):
        pos = len(b)-1-i
        if(b[pos]=='1'):
            n+= pow(2,i)
    return n

def select(poblation):
    element=""
    if len(indiv) == 0:
        for i in range(poblation):
            xt = random.randint(0,1000)%pow(2,b_x)
            yt = random.randint(0,1000)%pow(2,b_y)
            element = get_bin(xt, b_x) + get_bin(yt, b_y)
            #element = binary(xt, b_x)+binary(yt,b_y)
            indiv.append(element)
    else:
        Ssum = 0.00
        probab = []
        x = y = ""
        for i in range(poblation):
            x = copy(indiv[i],0,b_x-1)
            y = copy(indiv[i], b_x, b_y-1)
            t = fun(decimal(x), decimal(y))
            Ssum = Ssum+t
            probab.append(t)
            
        Ssum = Ssum/poblation
        for i in range(poblation):
            probab[i] = round(probab[i]/Ssum)
        for i in range(poblation):
            for j in range(1,probab[i]):
                indiv.append(indiv[i])
        for i in range(poblation-1,0,-1):
            if probab[i] == 0:
                indiv[i] = indiv[len(indiv) -1]
                indiv.pop()
        if len(indiv) > poblation:
            for i in range(len(indiv)-poblation):
                indiv.pop()
        if len(indiv) < poblation:
            for j in range(poblation-len(indiv)):
                indiv.append(indiv[j])
    return 1
def cross(e1,e2):
    t1=t2=""
    t = random.randint(0,1000)%(b_x+b_y)
    #T1
    t1 = copy(indiv[e1],0,t-1)
    t1 = t1 + copy(indiv[e2],t,b_x+b_y-1)
    #T2
    t2 = copy(indiv[e2],0,t-1) 
    t2 = t2+ copy(indiv[e1],t,b_x+b_y-1)
    #
    indiv[e1] = t1
    indiv[e2] = t2
    return 1
def maximize(poblation, times):
    for i in range(0,times):
        select(poblation)
        print("\n Iteration",i ," Indiv size",len(indiv), "\n" )
        #Graph x-generation y-fitness_value
        pty = [decimal(p) for p in indiv]
        #print(pty)
        py = 0 
        for j in pty:
            py+=j
        
        py = py/(len(indiv))
        px = i#[i for p in indiv];
        print("px,py: ",px," ",py)
        plt.plot(px,py, marker = 'D')#, linestyle = 'None')
        
        for j in range(0, poblation,2):
            cross(j,j+1)
        #for j in range(0, len(indiv)):
         #   print("\n indiv[",j,"]",indiv[j])
    plt.title('Mean/Generation')
    plt.show()
    return 1
def main():
    #print(len(indiv))
    maximize(100,20)
    
if __name__ == '__main__':
    main()

        
            


        
        