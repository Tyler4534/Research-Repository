# Introducing what the program is.
print("Welcome To The Quiz! ")

# A reminder note to use lowercases so no errors occur.
print("\n **NOTE** \n Note: Make sure to use lowercases at all times through answering the questions that don't involve numbers.")

# Asking the user for a input of what there name is.
name = input("\n Please Enter your name: ")

# Greeting the user with there name.
print("\n Hello", name + "!")

# Asking the user if they would like to start the quiz or not
user = input("\n Would you like to start the quiz? yes or no ")
# if the user types yes the program will continue to start the quiz
if user == ("yes"):
# Letting the user know that the quiz/program has started from the previous input of "yes".
  print("\n Alright, Let's begin!" )
   #  else is used if the condition is no.
else:
  # If user input equal to "no" then
  user == ("no ")
  # Then from the users input of "no" program says good bye to the name that they enetered in and have a nice day
  user = input('\n Good bye '   +  name  +  ' have a nice day! ')
  
  
# From yes program continues here answer_(num) input is asking for user input to answer the question   (Line 28 repeats on line: 39,46,53,60,69,75)
answer_1 = input("\n Q1 - How many countries are their in the world: ")
# If the user gets answer_(num)  answer correct it will be equal to the correct answer example for answer_1 == "195": (Line 30 repeats on line: 40,47,54,61,70,76)
if answer_1 == "195":
  # If user types the correct answer it'll print out a message saying that they're correct. (Line 32 repeats on line: 41,48,55,62,71,77)
  print("You're correct, There are 195 countries! ")
# If answer isn't equal to correct answer else statement would be used to print its an incorrect answer to the question (Line 34 repeats on line:42,49,56,63,72,78)
else:
 # If user's answer incorrect it will print that it is incorrect and give them the right answer. (Line 36 repeats on line: 43,50,57,64,73,79
  print(f"Incorrect! The answer is 195, not {answer_1!r}")
  

answer_2 = input("\n Q2 - How many continents are there in the world: ")
if answer_2 == "7":
  print("You're a correct! There are 7 cotinents! ")
else:
    print(f"Incorrect! The answer is 7, not {answer_2!r} ")

  
answer_3 = input("\n Q3 - What is the largest country in the world: ")
if answer_3 == "russia":
  print("You're correct! Russia is the largest country in the world. ")
else:
  print(f"You're Incorrect! Russia is the largest country in the world, not {answer_3!r}")

  
answer_4 = input("\n Q4 - Which country has the largest population in the world: ")
if answer_4 == "china":
  print("You're correct! China has the largest population in the world. ")
else:
  print(f"You're incorrect! China has the largest population in the world, not {answer_4!r}")

  
answer_5 = input("\n Q5 -  What is the hottest continent in the world: ")
if answer_5 == "africa":
  print("You're correct! Africa is the hottest continent. ")
else:
  print(f"You're Incorrect! Africa is the hottest continent, not {answer_5!r}")
  
# Note to tell the user to with north or south so then it's kept simple and easy for no errors to occur when user is answering this question.
print("\n Note: Respond with north or south")
  
answer_6 = input("\n Q6 -  Which is colder North pole or South pole: ")
if answer_6 == "south":
  print("You're correct! South pole is alot colder than the North pole")
else:
  print(f"You're Incorrect! South pole is colder, not {answer_6!r}")

answer_7 = input("\n Q7 - What river flows through the rainforest in brazil: ")
if answer_7 == "amazon":
  print("You're correct! It is the amazon river. ")
else:
  print(f"You're Incorrect! It is the amazon river, not {answer_7!r}")
# Once the user has finished answering all the questions it tells the user that they have completed the quiz. 
print("\n You have completed the quiz, Good bye! ")

 # https://stackoverflow.com/questions/32041840/python-error-typeerror-input-expected-at-most-1-arguments-got-3

  #https://pythonguides.com/python-ask-for-user-input/

  # https://realpython.com/python-quiz-application/

  



  

  




