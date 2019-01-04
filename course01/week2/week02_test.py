
def int_to_strings(iter):
    result = []
    for i in iter:
        result.append(str(i))
    return result


d = [1, 2, 4, 5, 674]
s = list(map(str, d))
print(type(s))
print(s)
print(int_to_strings(d))
