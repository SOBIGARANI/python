n=int(input())
a=input().split()
ar=[]
for i in a:
  ar.append(int(i))
for i in range(0,n):
  c=0
  for j in range(i+1,n):
    if(ar[i]==ar[j]):
      c=c+1
  if(c==0):
    
