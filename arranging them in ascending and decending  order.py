# Write a program to sort a dictionary in ascending or descending according to its values .
import operator 
d={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}

s= dict(sorted(d.items(), key=operator.itemgetter(1)))

print('ascending order : ',s)
s1= dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))

print('descending order : ',s1)


