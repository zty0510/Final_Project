def a():
    b = '{:0b}'.format(976)
    b = [ int(x) for x in list(b) ]
    return b


print( a())