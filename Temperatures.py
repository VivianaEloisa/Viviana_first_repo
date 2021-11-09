def fahr_to_cels(a):
    return (a-32)/1.8
def cels_to_fahr(b):
    return(b*1.8)+32
c=50
d=10
print("{0} °F is {1}°C.".format(c,fahr_to_cels(c)))
print("{0}°C is {1}°F.".format(d,cels_to_fahr(d)))
