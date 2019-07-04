nk=input().split()
k=int(nk[1])
a=input().split()
ar=[]
s=0
for i in a:
  ar.append(int(i))
for i in range(k+1):
  s=s+ar[i]
print(s)
