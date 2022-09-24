
def f(x):
    if ( x > 50  ):
        return x - 5
    return f(f(x+10));
    
print(f(10))   