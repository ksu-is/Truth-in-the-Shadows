def girlInteraction():
    print("You walk up to the girl. She looks up at you, sticks her tongue out, and runs off into the distance.")
    print("You start to follow the girl.")

def storeInteraction():
    print("You walk into the convenience store.")
    print("A large lollipop is 50% off for $5!")
    print("You get a weird feeling about this store.")

def strangerInteraction():
    print(f"You walk up to the stranger and ask if they have seen {friendName}.")
    print("The stranger stares at you for a while, then turns to look at an arcade down the road.")
    print("You thank the stranger, and start walking down.")

def backpackInteraction():
    print("You walk to your backpack and look inside.")
    print("You see a notepad and pencil inside! As well as a 5 dollar bill!")
    print("You put on the backpack and leave your apartment.")

def appleInteraction():
    print("You walk to the apple sitting on your desk.")
    print("You pick it up and put it into your pocket.")
    print("You leave your apartment.")

def apartmentExit():
    print("You leave your apartment.")
    secondChoiceLeaveApartment()

def apartmentReturn():
    print("You go back into your apartment. It's still quiet... too quiet.")

def firstChoice():
    directions = ["left", "right", "forward"]
    userInput = ""
    print(f"You just got off the phone with {friendName}'s mom.")
    print("To your left, you see your backpack. To your right, you see an apple. In front of you, you see the apartment door exit.")
    print("What would you like to do?")



    while userInput not in directions:
        print("Options: left/right/forward")
        userInput = input().lower().strip()
        if userInput == "left":
            backpackInteraction()
        elif userInput == "right":
            appleInteraction()
        elif userInput == "forward":
            apartmentExit()
        else:
            print("Please enter a valid option.")
    secondChoiceLeaveApartment()

def secondChoiceLeaveApartment():
    directions = ["left", "right", "forward", "backward"]
    userInput = ""
    print("You leave your apartment. To your left, you see a little girl holding a balloon. To your right, you see a convenience store. In front of you, you see a stranger in a black hoodie.")
    print("Where would you like to go?")

    while userInput not in directions:
        print("Options: left/right/forward/backward")
        userInput = input().lower().strip()
        if userInput == "left":
            girlInteraction()
        elif userInput == "right":
            storeInteraction()
        elif userInput == "forward":
            strangerInteraction()
        elif userInput == "backward":
            apartmentReturn()
        else:
            print("Please enter a valid option.")

# Start Here: What is your Name?
if __name__ == "__main__":
    print("Welcome to Truth in the Shadows! This is made by Nikky Hoffman.")
    print("You have been trying to contact your friend for the past week. One day, your friend's mom calls you, asking if you have seen your friend.")
    print("It turns out that your friend said they were staying at your place. That doesn't sound right. Something seems off.")
    print("Let's take a look around the city and see if we can find your friend.")
    
    print("But first: What is your name?")
    yourName = input()
    
    print(f"Welcome {yourName}!")
    print("Now: What is your friend's name?")
    friendName = input()
    
    print(f"Let's go find {friendName}!")
    firstChoice()
