n=int(input())
a=input().split()
s=""
ar=[]
for i in a:
  ar.append(int(i))
ar.sort()
ar=ar[::-1]
for i in ar:
  s=s+str(i)+""
print(s)
