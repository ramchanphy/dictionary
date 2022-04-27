dict={'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
a,b,c=dict.keys()
print(a,b,c)
x,y,z=dict.values()
f=x,y,z
i=0
while i<len(f):
    print(x[i],y[i],z[i])
    i=i+1