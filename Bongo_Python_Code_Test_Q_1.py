def dict_depth(dic, depth=1):
    for key in dic.keys():
        print(key, depth)
        if type(dic[key]) is dict:
            newdict = dic[key]
            return dict_depth(newdict, depth + 1)
    return depth


a = {
    'key1': 1,
    'key2': {
        'key3': 1,
        'key4': {
            'key5': 4,
        }
    }
}
b = {
    'key1': 1,
    'key2':
        {
            'key3': 1,
            'key4': 2
        }
}

print('For Dictionary a')
dict_depth(a, 1)
print('For Dictionary b')
dict_depth(b, 1)