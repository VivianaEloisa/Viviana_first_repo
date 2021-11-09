def feets_to_meters(a):
    return (a*0.3048)
def meters_to_feet(b):
    return(b/0.3048)
c=50
d=10
print("{0} feets are {1} meters.".format(c,feets_to_meters(c)))
print("{0} meters are {1} feets.".format(d,meters_to_feet(d)))
