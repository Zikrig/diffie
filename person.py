from random import randint as randint
import math

class person:
    def __init__(self,pg=[0,0]):
        self.a = randint(100,1000)
        if(pg[0])!=0:
            self.p,self.g=pg
        else:
            self.p, self.g = gen()
        self.keyA=stost(self.g,self.a,self.p)
        self.keyB=0
        self.K=0
        pass
    def ch(self,B):
        self.keyB=B
        self.K=stost(self.keyB,self.a,self.p)
        print(self.keyB,self.a,self.p)
        pass

def stost(a,b,delit):#Возведение в степень с остатком
    res=1
    for i in range(b):
        res*=a
        res = res % delit
    return (res)


def isSimple(a):        # проверка на простоту
    for c in range(2,int(math.sqrt(a))):
        if a%c==0:
            return 0
    return 1

def gen():
    l=randint(22,71)
    while(1):
        l+=1
        primR=primRoots(2*l+1)
        if(isSimple(l) and (isSimple(2*l+1)) and primR!=0):

            return (2*l+1, primR)


def sqr(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def primRoots(modulo):
    roots = []
    required_set = set(num for num in range (1, modulo) if sqr(num, modulo) == 1)

    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range (1, modulo))
        if required_set == actual_set:
            roots.append(g)
    res=0
    for res in roots:
        if(isSimple(res)):
            break
    return res
