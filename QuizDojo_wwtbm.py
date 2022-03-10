from time import sleep
from random import randint

#inspired on book.

status = "on"
money = 0
help_score = 2
jokers = ["A) The 50/50", "B) The Audience", "C) The Telephone"]

def ask_question(question, answers, correct, amount, audience, phone):
  print(question)
  sleep(3)
  for answer in answers:
    print(answer)
    sleep(1)
  user_answer = input("What is your answer?(A-D or J for joker) ")
  if user_answer.upper() == "J":
    use_joker(correct, amount, audience, phone)
  elif user_answer.upper() == correct:
    print(" ")
    correct_answer(amount)
    sleep(2)        
  else:
    global help_score
    if help_score > 0:
      help()
      for answer in answers:
        print(answer)
        sleep(1)
      user_answer2 = input("What is your answer?(A-D or J for joker) ")
      if user_answer2.upper() == "J":
        use_joker(correct, amount, audience, phone)
      elif user_answer2.upper() == correct:
        print(" ")
        correct_answer(amount)
        sleep(2)
      else:
        print(" ")
        game_over()
    else:
      print(" ")
      game_over()

def correct_answer(amount):
  sleep(1)
  print("That is...")
  sleep(1)
  print("CORRECT!!")
  print(" ")
  sleep(1)
  print("*applause*")  
  global money
  money = amount
  print(" ")
  sleep(1)
  print(f"Very well done {name}, you just won ${money}!")
  print(" ")
  sleep(1)

def use_joker(correct, amount, audience, phone):
  print(" ")  
  global jokers
  if len(jokers) == 0:
    print("Sorry, you have no jokers left!")
    sleep(2)
    user_answer = input("What is your answer? ")
    if user_answer.upper() == correct:
      print(" ")
      correct_answer(amount)
      sleep(2)
    else:
      print(" ")
      game_over()    
  else:    
    print("You have the following jokers:")
    sleep(2)
    for joker in jokers:
      print(f"{joker}-Joker")
      sleep(1)
    joker_selection = input("Which joker would you like to use?")
    if joker_selection.upper() == "A":
      jokers.remove("A) The 50/50")
      jokerA(correct, amount)
    elif joker_selection.upper() == "B":
      jokers.remove("B) The Audience")
      jokerB(correct, amount, audience)
    elif joker_selection.upper() == "C":
      jokers.remove("C) The Telephone")
      jokerC(correct, amount, phone)

def jokerA(correct, amount):
  answers = ["A", "B", "C", "D"]
  joker_answer = [correct]  
  answers.remove(correct)
  number = randint(0, 2)
  joker_answer.append(answers[number])
  joker_answer.sort()
  sleep(1)
  print(".")
  sleep(1)
  print("..")
  sleep(1)
  print("...")
  sleep(1)  
  print(f"The remaining answers are {joker_answer[0]} and {joker_answer[1]}")
  sleep(3)
  user_answer = input("What is your answer? ")
  if user_answer.upper() == correct:
    print(" ")
    correct_answer(amount)
    sleep(2)
  else:
    print(" ")
    game_over()

def jokerB(correct, amount, audience):
  sleep(1)
  print(".")
  sleep(1)
  print("..")
  sleep(1)
  print("...")
  sleep(1)
  print(f"The audience vote is: {audience}")
  sleep(3)
  user_answer = input("What is your answer? ")
  if user_answer.upper() == correct:
    print(" ")
    correct_answer(amount)
    sleep(2)
  else:
    print(" ")
    game_over()

def jokerC(correct, amount, phone):
  sleep(1)
  print(".")
  sleep(1)
  print("..")
  sleep(1)
  print("...")
  sleep(1)
  print(f"Here is what your Telephone Joker said:")
  sleep(1.5)
  print(phone)
  sleep(3)
  user_answer = input("What is your answer? ")
  if user_answer.upper() == correct:
    print(" ")
    correct_answer(amount)
    sleep(2)
  else:
    print(" ")
    game_over()

def help():
  global help_score
  help_score -= 1
  sleep(1.5)
  print(" ")
  print("...are you SURE that is correct?")
  sleep(2)
  print("again the possibilities are:")
  sleep(2)    

def game_over():
  global status
  status = "off"
  print("That is...")
  sleep(1)
  print("wrong!")
  print(" ")
  sleep(1)
  print(f"sorry {name}, you lost!")
  print(" ")
  print(" ")
  sleep(1)
  print("GAME OVER!")

question1 = "FIRST, THE $50 QUESTION: What is the biggest currency in Europe?"
answers1 = ["A) Afro", "B) Asio", "C) Australio", "D) Euro"]
correct1 = "D"
amount1 = 50
audience1 = ["A: 0%", "B: 2%", "C: 0%", "D: 98%"]
phone1 = "Haha, are you kidding me? The answer is D!"

question2 = "THE $100 QUESTION: Which of these kills its victims by constriction?"
answers2 = ["A) Andalucia", "B) Anaconda", "C) Andypandy", "D) Annerobinson"]
correct2 = "B"
amount2 = 100
audience2 = ["A: 2%", "B: 95%", "C: 2%", "D: 1%"]
phone2 = "Come on! Im sure the answer is B!"

question3 = "NOW THE $200 QUESTION: In the UK, VAT stands for value-added ...?"
answers3 = ["A) Transaction", "B) Total", "C) Tax", "D) Trauma"]
correct3 = "C"
amount3 = 200
audience3 = ["A: 15%", "B: 10%", "C: 75%", "D: 0%"]
phone3 = "Oh, umm, isn't it C? I think it is C. Yes, try C!"

question4 = "OUR $300 QUESTION: What might an electrician lay?"
answers4 = ["A) Tables", "B) Gables", "C) Cables", "D) Stables"]
correct4 = "C"
amount4 = 300
audience4 = ["A: 28%", "B: 3%", "C: 68%", "D: 1%"]
phone4 = "Well... an electrician uses cables, so C right?"

question5 = "THE $500 QUESTION: How is a play on words commonly described?"
answers5 = ["A) Pan", "B) Pin", "C) Pen", "D) Pun"]
correct5 = "D"
amount5 = 500
audience5 = ["A: 21%", "B: 12%", "C: 19%", "D: 48%"]
phone5 = "Oh, a play on words... is it A or D? I think D."

question6 = "$1,000 QUESTION: Which colour is used as a term to describe an illegal market for rare goods?"
answers6 = ["A) Black", "B) Blue", "C) Red", "D) White"]
correct6 = "A"
amount6 = 1000
audience6 = ["A: 58%", "B: 4%", "C: 21%", "D: 17%"]
phone6 = "I know that black markets exists, I have heard of that. I don't know what they are though... go with A!"

question7 = "OUR $2,000 QUESTION: Which character was first played by Arnold Schwarzenegger in a 1984 film?"
answers7 = ["A) The Demonstrator", "B) The Instigator", "C) The Investigator", "D) The Terminator"]
correct7 = "D"
amount7 = 2000
audience7 = ["A: 4%", "B: 3%", "C: 11%", "D: 82%"]
phone7 = "It is his most famous movie! The answer is D!"

question8 = "NEXT, THE $4,000 QUESTION: In which country would you expect to be greeted with the word 'bonjour'?"
answers8 = ["A) France", "B) Italy", "C) Spain", "D) Wales"]
correct8 = "A"
amount8 = 4000
audience8 = ["A: 72%", "B: 12%", "C: 14%", "D: 2%"]
phone8 = "Isn't that french? So A should be the answer, right?"

question9 = "OUR $8,000 QUESTION: What name is given to the person who traditionally attends the groom on his wedding day?"
answers9 = ["A) Best man", "B) Top man", "C) Old man", "D) Poor man"]
correct9 = "A"
amount9 = 8000
audience9 = ["A: 48%", "B: 38%", "C: 14%", "D: 0%"]
phone9 = "It is either A or B, I am not sure though..."

question10 = "NOW FOR $16,000: People who are in a similar unfavourable situation are said to be 'all in the same ...'?"
answers10 = ["A) Train", "B) Plane", "C) Boat", "D) Tube"]
correct10 = "C"
amount10 = 16000
audience10 = ["A: 15%", "B: 8%", "C: 77%", "D: 0%"]
phone10 = "all in the same boat I think: try C!"

question11 = "$32,000 FOR THIS ONE: According to the old adage, how many lives does a cat have?"
answers11 = ["A) Five", "B) Seven", "C) Nine", "D) Ten"]
correct11 = "C"
amount11 = 32000
audience11 = ["A: 17%", "B: 42%", "C: 39%", "D: 2%"]
phone11 = "Ohh... I don't know if it is B or C. Definately not D."

question12 = "THE $64,000 QUESTION: How many countries use the Euro as their currency?"
answers12 = ["A) 12", "B) 16", "C) 19", "D) 28"]
correct12 = "C"
amount12 = 64000
audience12 = ["A: 19%", "B: 26%", "C: 28%", "D: 27%"]
phone12 = "I am terribly sorry but I have no idea."

question13 = "$125,000 QUESTION: How many different time zones exist within Russia?"
answers13 = ["A) 8", "B) 7", "C) 6", "D) 5"]
correct13 = "A"
amount13 = 125000
audience13 = ["A: 38%", "B: 26%", "C: 21%", "D: 15%"]
phone13 = "Russia?! How would I know?! The country is huge, must be a lot."

question14 = "OUR $500,000 QUESTION: California has alomost the same population as..."
answers14 = ["A) The United Kingdom", "B) Spain", "C) Italy", "D) Poland"]
correct14 = "D"
amount14 = 500000
audience14 = ["A: 9%", "B: 31%", "C: 11%", "D: 49%"]
phone14 = "I have no idea. Which country is the smallest? The smallest one is probably correct."

question15 = "AND NOW: THE FINAL $1,000,000 QUESTION!!!!! How many Game Boys were sold world wide?"
answers15 = ["A) over 50 Million", "B) over 100 Million", "C) over 500 Million", "D) over one Billion"]
correct15 = "B"
amount15 = 1000000
audience15 = ["A: 32%", "B: 29%", "C: 28%", "D: 11%"]
phone15 = "I have absolutely no clue! But wait, one billion cannot be right, can it? How many people live on the earth?!"

print(" ")
print(" ")
print(" ")  
print("Ladies and Gentlemen!")
print(" ")
sleep(1.3)
print("Welcome to a new round of")
print(" ")
sleep(0.7)
print("WHO")
sleep(0.7)
print("WANTS")
sleep(0.7)
print("TO")
sleep(0.7)
print("BE")
sleep(0.7)
print("A")
sleep(0.7)
print("MILLIONAIRE?!")
print(" ")
sleep(1.3)
print("*applause*")
print(" ")
sleep(2.5)

print("OUR FIRST CANDIDATE TONIGHT IS ....")
sleep(1.5)
print("...ehm...")
print(" ")
sleep(1.5)
name = input("sorry, I forgot your name. What is your name? (enter your name) ")
print("Of course that is your name!")
print(" ")
sleep(1.5)
print(f"Everyone, a BIG ROUND OF APPLAUSE FOR OUR CANDIDATE {name.upper()}!")
print(" ")
sleep(2)
print("*big round of applause*")
print(" ")
sleep(2)

print("ok, let's get started. First a reminder, you have 3 jokers:")
sleep(2)
for joker in jokers:
  print(f"{joker}-Joker")
  sleep(1.5)
print("You can only use ONE joker for each question.")
sleep(2.5)
print(" ")
print(" ")
print("OK, let's go!")
print(" ")
print(" ")
sleep(1.5)

ask_question(question1, answers1, correct1, amount1, audience1, phone1)

if status == "on":
  ask_question(question2, answers2, correct2, amount2, audience2, phone2)

if status == "on":
  ask_question(question3, answers3, correct3, amount3, audience3, phone3)

if status == "on":
  ask_question(question4, answers4, correct4, amount4, audience4, phone4)

if status == "on":
  ask_question(question5, answers5, correct5, amount5, audience5, phone5)

if status == "on":
  ask_question(question6, answers6, correct6, amount6, audience6, phone6)

if status == "on":
  ask_question(question7, answers7, correct7, amount7, audience7, phone7)

if status == "on":
  ask_question(question8, answers8, correct8, amount8, audience8, phone8)

if status == "on":
  ask_question(question9, answers9, correct9, amount9, audience9, phone9)

if status == "on":
  ask_question(question10, answers10, correct10, amount10, audience10, phone10)

if status == "on":
  ask_question(question11, answers11, correct11, amount11, audience11, phone11)

if status == "on":
  ask_question(question12, answers12, correct12, amount12, audience12, phone12)

if status == "on":
  ask_question(question13, answers13, correct13, amount13, audience13, phone13)

if status == "on":
  ask_question(question14, answers14, correct14, amount14, audience14, phone14)

if status == "on":
  ask_question(question15, answers15, correct15, amount15, audience15, phone15)

if status == "on":
  print("CONGRATULAAAAAAAAAAAAATIONS!!!!!!")
  sleep(2)
  print(" ")
  print("YOU ARE THE WINNER OF ")
  sleep(2)
  print("ONE")
  sleep(1)
  print("MILLION!!")
  sleep(1)
  print("DOLLARS!!!!!!!!!!!!!!!!")
  print(" ")
  print(" ")
  sleep(2)
  print("OUR LATEST MEMBER IN THE ALL TIME HALL OF FAME...")
  print(" ")
  sleep(3)
  print("IS...")
  print(" ")
  sleep(1.5)
  print("THE UNFORGETABLE NEW MILLIONAIRE: ")
  print(" ")
  sleep(3)
  print(f"{name.upper()}!!!")
  sleep(1.5)
  print(f"*incredibly loud applause and cheering*")
  sleep(1.5)
  print(f"   {name.upper()}!!!")
  sleep(1)
  print(f"   {name.upper()}!!!")
  sleep(1)
  print(f"   {name.upper()}!!!")
  sleep(1)
  print(f"   {name.upper()}!!!")
  sleep(1)
  print("   ...")
  sleep(3)
  print(" ")
  print(" ")
  print(" ")
  print("THE END")





