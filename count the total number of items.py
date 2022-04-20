# Count the total number of items from the values of the dictionary which
# are in the form of a list.
dict1 =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
count = 0
for x in dict1:
   if isinstance(dict1[x], list):
      count += len(dict1[x])
print("total count: ",count)
