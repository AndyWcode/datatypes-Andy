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



usernumber = int(input(" What whole number would you pick: "))

def allfactors(usernumber):
    factorlist = []
    for number in range(1, usernumber):
        if  usernumber % number == 0:
            factorlist.append(number)
    for number in factorlist:
        print(number)
            
            
allfactors(usernumber)

            
        
           
            
    
    
    
            




