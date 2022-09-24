# 1. Argument: Python allows function arguments to have default values. 
# If the function is called without the argument, the argument gets its default value.
# 2.Variable scope: Pycharm says: "Default argument value is mutable."
# That's the problem: the value you provide as the default (the empty list) is an actual list, and like any other list, 
# you can change it and if multiple variables have that list as a value, those changes will show up for all of them.
# Instead of passing "l = []", use "l = None"

def f(i, l = []):
    l.append(i)
    return l

f(1)
f(2)
x = f(3)
print(x)

