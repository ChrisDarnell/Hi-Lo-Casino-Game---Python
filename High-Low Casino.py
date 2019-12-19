import time, os, random

# Welcome 

print("Welcome to my High-Low Game.")
print("Test fate and see how long you can guess the next card before failing!")
print("Ace is high. Draw goes to the house.")
time.sleep(3)

# Deck Setup

ranks = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King", "Ace"]
suits = ["Clubs","Hearts","Diamonds","Spades"]
deck = []

value = 1
for rank in ranks:
    for suit in suits:
        deck.append([rank + " of " + suit, value])
    value = value + 1

# Get 1st Card

random.shuffle(deck)
score = 0
card1 = deck.pop(0)


while True:
    os.system("cls") 
    print("Your score is", score)
    print("\n\nCurrent card:", card1[0])
    while True:
        choice = input("Will the next card be Higher or Lower? ")
        if len(choice) > 0:
            if choice[0].lower() in ["h","l"]:
                break
   
# Get 2nd Card

    card2 = deck.pop(0)
    print("The next card is", card2[0])
    time.sleep(1)


    if choice[0].lower() == "h" and card2[1] > card1[1]:
        print("Yes, it is higher! You get a point.")
        score +=1
        time.sleep(1)
    if choice[0].lower() == "h" and card2[1] < card1[1]:
        print("It is lower. Noooooo!")
        time.sleep(1)
        break
    if choice[0].lower() == "l" and card2[1] < card1[1]:
        print("Yes, it is lower! You get a point!")
        score +=1
        time.sleep(1)
    if choice[0].lower() == "l" and card2[1] > card1[1]:
        print("It is higher. Nooooo!")
        time.sleep(1)
        break
    if card2[1] == card1[1]:
        print("Draw! House wins.")
        break

# Compare against newest drawn card

    card1 = card2

# Results

os.system("cls")
print("You have lost. Loser!")
print("Your longest sequence was", score)

# Play Again?

another = input("Try again? Yes or No? ")
if len(another) > 0:
    if another[0].lower() in ["y","n"]:
      if another[0].lower() == "y":
          print("Cool! Launch again!")
      if another[0].lower() == "n":
          print("Cool! Thanks for playing!")
time.sleep(4)
os.system("cls")