# Write a program remove the first key value pair from a nested dictionary.
dic={
    1:"NAVGURUKUL",
    2:"IN",
    "name":{"A":{"apple":{"WELCOME":"wel","B":"TO","C":"DHARAMSALA"}}}}
# del dic[3]["A"]
# print(dic)
print(dic["name"]["A"]["apple"]["WELCOME"])