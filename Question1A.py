
l1=["HTTP","HTTPS","FTP","DNS"]
l2=[80,443,20,53]

D={}
for i in range(len(l1)):
    D[l1[i]]=l2[i]
print(D)