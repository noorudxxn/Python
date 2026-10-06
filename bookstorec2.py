
book1 = "\t{} - ₹{}".format("Python Basics", 450)
book2 = "\t{} - ₹{}".format("Data Science Intro", 600)

total = 450 + 600
total_line = "\t{} - ₹{}".format("Total", total)

message = "\n\tThank you for shopping with us!"

receipt =  book1 + "\n" + book2 + "\n" + total_line + message

print(receipt.upper())