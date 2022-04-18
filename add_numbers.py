# **first method
dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
for key in dic2:
    if key in dic1:
        dic2[key]=dic2[key]+dic1[key]
d={**dic1,**dic2,**dic3}
print(d)


 



