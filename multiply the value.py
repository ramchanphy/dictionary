# Q14.Write a Python program to multiply all the items in a dictionary.
d={"age":19,"class":12}
mul=1
for i in d:
    mul=mul*d[i]
print(mul)