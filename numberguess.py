import random
print("*" * 30)
print("     WELCOME TO PYTHON")
print("*" * 30)
print("""
╔════════════════════════════╗
║     GUESS THE NUMBER       ║
╠════════════════════════════╣
║     You have 7 chances!    ║
╚════════════════════════════╝
""")
randomnum = random.randint(1,100)
for i in range(7):
      while True:
        try:
            guessnum = int(input("Enter the number : "))

            if guessnum < 1 or guessnum > 100:
                print("Enter a number between 1 and 100.")
                continue

            break

        except ValueError:
            print("Invalid input! Please enter an integer.")

        if guessnum == randomnum:
            print("winner")
            break
        elif guessnum > randomnum:
                print("Too High")
        elif guessnum < randomnum:
                print("Too Low")
                if i== 6:
                    print("you have no attemts left")
                    print("THE NUMBER IS ",randomnum)

