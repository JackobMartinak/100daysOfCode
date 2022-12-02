print("Welcome to the Tresura Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at crossroad, where do you want to go? "left" or "right"?.').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim accross').lower()
    if choice2 == "swim":
        print("")
    else:
        print("")
else: 
    print("You fell into a hole. Game Over.")
