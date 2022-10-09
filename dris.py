#questions
#1
import math


num=[1,2,3,4,5,6]
x=list(map(lambda i:(i+i+i),num))
print(x)

#2







#3
def str(s):
    return s.lower()
str_std=["WELCOME","TO","SEM3"]
x=list(map(str,str_std))
print(x)

#4
def square(s):
    return math.sqrt(s)
num=[4,9,16,25,36,49,64,81]
sqr=list(map(square,num))
print(sqr)


#5






#6
def table(i):
    return i*7
num=[1,2,3,4,5,6,7,8,9,10]
tab=list(map(table,num))
print(tab)


#7
a=[1,3,5,7,9]
b=[2,4,6,8,10]
c=list(map(lambda x,y:(x+y),a,b))
print(c)


#8
def float(i):
    return int(i)
num=[2.0,3.0,4.0,5.0]
x=list(map(float,num))
print(x)

#9




#10
def abc(d):
    return d.lower()
dictio={'a':'DRISHTI','b':'SRISHTI','c':'RIDDHI'}
dt=dict(map(abc,dictio))
dicti=dict(map(lambda d:(d[0],d[1]+'@gmail.com'),dictio.items()))
print(dt)
print(dicti)