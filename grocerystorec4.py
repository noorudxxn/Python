fruits = ["apple", "orange","grapes"]
vegetables = ["carrot","cucumber","tomato"]
beverages = ["cola","pepsi" , "campa"]
print(fruits)
print(vegetables)
print(beverages)
fruits.append("banana")
vegetables.insert(1,"potato")
del beverages[2]
print(beverages)
inventory = [fruits,vegetables,beverages]
print(inventory)
print(fruits[:2])
print(vegetables[-1:])
lenths = [len(x) for x in fruits]
print(lenths)
print("water" in beverages)
new_tup = (fruits[0],vegetables[0],beverages[0])
print(new_tup)
