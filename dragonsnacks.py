print("you are in a dark room in a mystrious castle.")
print("In front of you are 3 doors. you have to choose one.")
playerChoice = input("Choose 1,2, or 3...")
if playerChoice == "1":
    print("you find a room full of gold. Your rich!")
    print("YOU WON!")
elif playerChoice == "2":
    print("the door opens and an angry oger hits you with his club")
    print("YOU LOST")
elif playerChoice == "3":
    print("you open the door and you find a sleeping dragon.")
    print("you can ether...")
    print("1, steal some of the dragons gold")
    print("or 2, try to sneek around the dragon")
if DragonChoice == "1":
    print("the dragon wakes up and eats you")
    print("YOU LOST")
elif DragonChoice == "2":
    print("you sneak around the dragon and escape the castle")
    print("YOU WIN!!!")
else:
    print("yove waited to long! uh oh,DRAGON!!! the dragon")
    print("ate you. YOU LOST.")
