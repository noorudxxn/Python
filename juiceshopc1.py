import random
applejuice = 15.5
orangejuice = 20
grapejuice = 10.25
total = applejuice + orangejuice + grapejuice 
print ("total volume = ",total,"liters ")
total_int = int(total)
total_string = str(total_int)
print("the total is " + total_string + "liters")
bonus = random.randint(5,10)
final_total = total + bonus
print("bonus liters : ",bonus)
print("final total: ",final_total)