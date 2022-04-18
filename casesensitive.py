# Dictionary keys should be case sensitive, means we can write keys with same
# names but different case. Python treats them as different keys.
Dict ={
    'ball' : 'green',
    'Ball': 'red'
}
print(Dict['ball'])
print(Dict['Ball'])
print(Dict['bat'])