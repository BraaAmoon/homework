L=['Network','Math','Programming','Physics','Music']
t=True
for i in range(len(L)):
    if t==L[i].startswith('Ph'):
        index=i
        item=L[i]
print('index:',i,"item",item)