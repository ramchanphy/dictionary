# Create a dictionary from 2 lists, where the elements of 1st list are the keys 
# and the elements of the 2nd list are the corresponding values.
list1=["one","two","three","four","five"]
list2=[1,2,3,4,5]
res = {}
for key in list1:
    for value in list2:
        res[key]
        res[key] = value
        list2.remove(value)
        break  
print(str(res))