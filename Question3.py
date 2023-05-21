import json

f1=open('D:\\project\\network programming\\homework1\\quiz .json','r')
d1=json.load(f1)
f1.close()
f2=open('D:\\project\\network programming\\homework1\\score.json','w')
d2={}
name=input("Enter your name: ")
d2['user name']=[name]
score=0
for key,val in d1.items():
    print(key)
    x=int(input("Enter your Answer: "))
    d2[key]=[x]
    if x==d1[key]:score+=1
d2["the score is: "]=score
json.dump(d2,f2)
f2.close()
print(d2)


