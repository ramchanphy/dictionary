# Write a program to print the top 3 highest values of a given dictionary.
my_dict={'a':58, 'b':50, 'c':56,'d':40, 'e':100, 'f':20}
a=[]
for i in my_dict:
    b=my_dict[i]
    a.append(b)
    a.sort()
print(a[3:])
    

