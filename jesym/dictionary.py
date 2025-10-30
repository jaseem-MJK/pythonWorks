my_dict = {'b': 3, 'a': 1, 'c':2}

asc = dict(sorted(my_dict.items()))
print("ascending order:",asc)

desc = dict(sorted(my_dict.items(), reverse=True))
print("descending order:" ,desc)
