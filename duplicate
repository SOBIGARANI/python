n=int(input())
a=input().split()
ar=[]
s=""
for i in a:
  ar.append(i)
for i in range(0,n-1):
  c=0
  for j in range(i+1,n-1):
    if(ar[i]==ar[j]):
      c=c+1
  if(c!=0 and (ar[i] not in s)):
    s=s+str(ar[i])+" "
if(s==""):
  print("Unique")
else:
  print(s)
