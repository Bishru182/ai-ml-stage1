thisDict={"id":1000, "name":"saman", "salary":2000 }
print(thisDict)
print(thisDict["id"])
print(type(thisDict))

# dictionaries are mutable
thisDict["id"]=3456
print(thisDict)

thisDict["address"]={"no":36, "street":"main road", "city":"puttalam"}
print((thisDict))
print(thisDict["address"]["no"])