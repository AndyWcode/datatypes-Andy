# usersentence = input(" Please input sentence: ")
# usersplit = usersentence.split()
# userwrdnm = len(usersplit)
# print(f"Your sentence: {usersentence} /////  has {userwrdnm} words")


# userinput = float(input("Input your number"))
# int(userinput)
# calc = userinput % 2
# if calc == 0:
#     print("even")
# else:
#     print("odd")



# def bad(userbill):
#         print(f" Your total is ${userbill}")

# def Okay(userbill):
#     usertotal = userbill + (userbill * .15 )
#     print(f" Your total bill is ${usertotal}.")

# def Good(userbill):
#     usertotal = userbill + (userbill * .20)
#     print(f" Your total is ${usertotal}.")

# def Great(userbill):
#     usertotal = userbill +(userbill * .25)
#     print(f"Your total is ${usertotal}.")

# userbill = float(input("How much was your bill?: "))
# while True:

#     userinput = input("How was the service? (Bad/Okay/Good/Great: ").upper()
#     if userinput == "BAD":
#         bad(userbill)
#         break
#     elif userinput =="OKAY":
#          Okay(userbill)
#          break
#     elif userinput =="GOOD":
#          Good(userbill)
#          break
#     elif userinput == "GREAT":
#          Great(userbill)
#          break
#     else:
#          print(" YOU HAVE TO EITHER TYPE BAD, OKAY, GOOD, OR GREAT!!")

import math

# def gcffinder():
#     usernumber1 = int(input(" What will be your first whole number?: "))
#     usernumber2 = int(input(" What is your second whole number?: "))
#     gcf = math.gcd(usernumber1, usernumber2)
#     print(gcf)



# usernumber = int(input(" What whole number would you pick: "))

# def allfactors(usernumber):
#     factorlist = []
#     for number in range(1, usernumber+ 1):
#         if  usernumber % number == 0:
#             factorlist.append(number)
#     print("Factors")
#     print("//////")
#     for number in factorlist:
#         print(number)
#         print("//////")
            


import random
def guessgame():
        largestnm = 100
        guesses = 0 
        randomnumber = random.randint(1,largestnm)
        userguesshistory = []
        while True: 
            userguess = input("Input a number to guess!: ")
            
            if userguess.isdigit() == False:
                 print(f"NO LETTERS, PICK (1-{largestnm})")
            elif int(userguess) > largestnm:
                 print(f"You can only pick numbers 1-{largestnm}!!!!!")


            elif int(userguess) > randomnumber:
                print("pick a lower number!")
                userguesshistory.append(userguess)
                guesses += 1
            elif int(userguess) < randomnumber:
                print("pick a higher number!")
                userguesshistory.append(userguess)
                guesses += 1
            else:
                print(f" You guessed the CORRECT NUMBER OF {randomnumber}!!")
                print("YOUR WRONG GUESSES")
                print(userguesshistory)
                print(f"It took you {guesses} guesses!")
                break
            
             

guessgame()


            
        
           
            
    
    
    
            




