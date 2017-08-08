# map   python     keyword
hash_map = {} # or dict()
hash_map['shaun'] = 98
hash_map['wei'] = 99
exist = 'wei' in hash_map  # check existence
point = hash_map['shaun']  # get value by key
point = hash_map.pop('shaun') # remove by key, return value
keys = hash_map.keys()  # return key list
# iterate dictionary(map)
for key, value in hash_map.items():
    # do something with k, v
    pass