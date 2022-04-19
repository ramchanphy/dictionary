# Take a list having dictionary elements as shown below 
# (Sample Data) and then store all the unique values into a list and print.
d=[{"first":"1"}, {"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"}, {"six":"9"},{"seven":"7"}]
e={}
i=0
while i<len(d):
    e.update(d[i])
    i+=1
a=[]
for j in e:
    if e[j] not in a:
        a.append(e[j])
print(a)