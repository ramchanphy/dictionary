word="mississipi"
c={"m":0,"i":0,"s":0,"p":0}
for i in word:
    if i=="m":
        c["m"]+=1
    elif i=="i":
        c["i"]+=1
    elif i=="s":
        c["s"]+=1
    elif i=="p":
        c["p"]+=1
print(c)