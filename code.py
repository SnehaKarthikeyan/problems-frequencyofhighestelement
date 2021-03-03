Coding:
  
from array import *
def largest(arr,n): 
    max = arr[0]
    for i in range(1, n): 
        if arr[i] > max: 
            max = arr[i] 
    return max
a=input()
arr=list(map(int,input().split()))
n= len(arr) 
Ans = largest(arr,n) 
b=int(arr.count(Ans))
if b==1:
  print(Ans,"occurs",b,"time")
else:
  print(Ans,"occurs",b,"times")
