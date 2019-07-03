n=int(input())
a=input().split()
ar=[]
s=""
for i in a:
  ar.append(int(i))
for i in range(0,n):
  c=0
  for j in range(i+1,n):
    if(ar[i]==ar[j]):
      c=c+1
  if(c!=0):
    s=s+str(ar[i])+""
for i in s:
  while(int(i) in ar):
    ar.remove(int(i))
for i in ar:
  print(i,end=" ")
