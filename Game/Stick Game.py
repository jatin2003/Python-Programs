# Program to play Stick Game with Computer

# There are 21 sticks, you can take 1-4 number of sticks at a time
# Whoever will take the last stick will loose

sticks = 21

while True:
    print("Sticks left: " , sticks)
    sticks_taken = int(input("Take sticks(1-4):"))
    if sticks == 1:
        print("You took the last stick, You loose!")
        break
    if sticks_taken >= 5 or sticks_taken <= 0:
        print("Wrong choice!")
        continue
    print("Computer took: " , (5 - sticks_taken) , "\n")
    sticks -= 5
