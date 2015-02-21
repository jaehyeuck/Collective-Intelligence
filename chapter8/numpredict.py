from random import random,randint
import math

def wineprice(rating, age):
    pass

def wineset1():
    pass

def euclidean(v1, v2):
    pass

def getdistances(data, vec1):
    pass

def knnestimate(data, vec1, k=3):
    pass

def inverseweight(dist,num=1.0,const=0.1):
    return num/(dist+const)

def subtractweight(dist,const=1.0):
    if dist>const:
        return 0
    else:
        return const-dist

def gaussian(dist,sigma=10.0):
    return math.e**(-dist**2/(2*sigma**2))

def weightedknn(data,vec1,k=5,weightf=gaussian):
    pass

def dividedata(data,test=0.05):
    pass

def testalgorithm(algf,trainset,testset):
    pass

def crossvalidate(algf,data,trials=100,test=0.05):
    pass

def wineset2():
    pass

def rescale(data,scale):
    pass



def crossvalidate(algf,data,trials=100,test=0.05):
    pass

def wineset2():
    pass

def rescale(data,scale):
    pass



def crossvalidate(algf,data,trials=100,test=0.05):
    pass

def wineset2():
    pass

def rescale(data,scale):
    pass



def crossvalidate(algf,data,trials=100,test=0.05):
    pass

def wineset2():
    pass

def rescale(data,scale):
    pass

def createcostfunction(algf,data):
    def costf(scale):
        pass
    return costf

def wineset3():
    pass

def probguess(data,vec1,low,high,k=5,weightf=gaussian):
    pass

def probabilitygraph(data,vec1,high,k=5,weightf=gaussian,ss=5.0):
    pass



