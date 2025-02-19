data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

def calculate_structure_sum(*args):
    result = 0
    
    for i in args:
        if isinstance(i,(list, tuple, set)):
            result += calculate_structure_sum(*i)
        elif isinstance(i, dict):
            result += calculate_structure_sum(*i.items())
        elif isinstance(i, str):
            result += len(i)
        elif isinstance(i,(int,float)):
            result += i
        elif i is None:
            pass
    return result

print(calculate_structure_sum(data_structure))
