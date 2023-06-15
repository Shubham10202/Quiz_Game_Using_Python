print("Welcome to my computer quiz!!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay Let's Play :)")
score = 0

answer = input("Who is the father of computer science? ")
if answer.lower() == "charles babbage":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does GPU stand for? ")
if answer.lower() == "graphic processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What translates and executes program at run time line by line? ")
if answer.lower() == "interpreter":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("EEPROM stands for _______? ")
if answer.lower() == "electronic erasable programmable memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What converts an entire program into machine language? ")
if answer.lower() == "compiler":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")



answer = input("BIOS stands for _______? ")
if answer.lower() == "basic input output system":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("GUI stands for? ")
if answer.lower() == "Graphic user interface":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")




print("You got " + str(score) + " questions correct!")
print("You got" + str((score/10) * 100)+ "%.")





