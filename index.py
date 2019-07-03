n=int(input())
a=input().split()
s=""
ar=[]
for i in a:
  ar.append(int(i))
for i in range(0,n):
  if(i==ar[i]):
    s=s+str(ar[i])+" "
if(s==""):
  print(-1)
else:
  print(s)
