d={'bijender':45,'deepak':60,'param':20,"anjili":30,'roshini':50}
p=sorted(d.values())
a={}
for i in p:
    for j in d.keys():
        if d[j]==i:
            a[j]=i
print(a)


        
