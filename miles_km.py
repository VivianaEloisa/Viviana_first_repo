def mil_to_km(a):
    return (a/0.621371)
def km_to_mil(b):
    return(b*0.621371)
c=50
d=10
print("{0} miles are {1} kilometers.".format(c,mil_to_km(c)))
print("{0} kilometers are {1} miles.".format(d,km_to_mil(d)))
