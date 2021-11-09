rivers = ["Chagres", "Nile", "Amazon", "Rhine"]
    print (Rivers)
lenght = [1,2,3,4]
dictzip = dict(zip(rivers,lenght))
for x, (k,v) in enumerate(dictzip.items())
    print("The lenght of the river {0} is {1} km.".format(k,v))
