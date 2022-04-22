
#You can change the question and name according to your liking.
name = "Misbah"
question= "Will I be marrying sometime soon?"
answer = ""

import random
random_number= random.randint(1,12)
#Generates a random number for random answers each time
if random_number == 1:
  answer = ("Yes - definitely,")
elif random_number == 2:
  answer = ("It is decidely so")
elif random_number ==3:
  answer = ("Without a doubt.")
elif random_number ==4:
  answer = ("Reply hazy, try again")
elif random_number ==5:
  answer = ("Ask again later.")
elif random_number ==6:
  answer = ("Better not tell you now.")
elif random_number ==7:
  answer = ("My sources say no.")
elif random_number ==8:
  answer = ("Outlook not so good.")
elif random_number == 9: 
  answer = ('Very doubtful')
elif random_number == 10:
  answer =("Not possible, lol.")
elif random_number == 11:
  answer= ("In your dreams.")
elif random_number == 12:
  answer = ("One in a million chance")
else: answer = "Error"

if name == "": print("Question:",question)
else: print(name +  " asks: " + question)

if question =="": print("Error! You are trying something that isn't possible.")

else: print("Magic 8-Ball's answer: " + answer)
