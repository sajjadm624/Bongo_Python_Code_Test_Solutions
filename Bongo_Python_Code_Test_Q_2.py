def dict_depth(dic, depth):
    for key in dic.keys():
        print(key, depth)
        if type(dic[key]) is dict:
            newdict = dic[key]
            dict_depth(newdict, depth + 1)
        elif type(dic[key]) == Person:
            newobj=dic[key]
            obj_depth(newobj, depth)
    return depth


def obj_depth(obj, depth):
    for attr, value in vars(obj).items():
        print(attr, depth)
        if type(value) == Person:
            newobj=value
            obj_depth(newobj, depth+1)
    return depth


class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father


person_a = Person('User', '1', None)
person_b = Person('User', '2', person_a)


a = {
    'key1': 1,
    'key2': {
        'key3': 1,
        'key4': {
            'key5': 4,
            'user': person_b,
        }
    }
}


dict_depth(a, 1)