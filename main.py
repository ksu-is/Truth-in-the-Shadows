if __name__ == "__main__":
  while True:
    print("Welcome to Truth in the Shadows! This is made by Nikky Hoffman.")
    print("You have been trying to contact your friend for the past week.")
    print("One day, your friend's mom calls you, asking if you have seen your friend.")
    print("It turns out that your friend said they were staying at your place.")
    print("That doesn't sound right. Something seems off.")
    print("Let's take a look around the city and see if we can find our friend!")
    print("But first: What is your name?")
    yourName = input()
    print("Welcome " +yourName+ "!")
    friendName = input()
    print("Let's go find" +friendName+ "!")
    
    firstChoice()

def firstChoiceApartment():
  directions = ["left","right","forward","backward"]
  print("You just got off the phone with +friendName+ "/s" mom.")
  print("To your left, you see your backpack. To your right, you see an apple. In front of you, you see the apartment door exit.")
  print("Where would you like to do")
   userInput = ""
  while userInput not in directions:
    print("Options: left/right/forward")
    userInput = input()
    if userInput == "left":
      backpackInteraction()
    elif userInput == "right":
      appleInteraction()
    elif userInput == "forward":
      apartmentExit()
    else: 
      print("Please enter a valid option.")

def backpackInteraction
print("You walk to your backpack and look inside.")
print("You see a notepad and pencil inside! As well as a 5 dollar bill!")
print("You put on the backpack and leaves your apartment.")

def appleInteraction()
print("You walk to the apple sitting on your desk.")
print("You pick it up and put it into your pocket.")
print("You leave your apartment")



  def SecondChoiceLeaveApartment()
  directions = ["left","right","forward","backward"]
  print("You leave your apartment. To your left, you see a little girl holding a balloon. To your right, you see a convinence store. In front of you, you see a stranger in a black hoodie.")

