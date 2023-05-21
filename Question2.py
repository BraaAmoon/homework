x=input('Enter Binary Number:')
s=[]
for i in range(len(x)):
    c=int(x[i])
    s.extend([c])
dis=0
s.reverse()
for  i in  range(len(s)):
    
    dis+=(s[i]*(2**i))
    
print(dis)

