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




def findgcf():
    usernum1 = int(input("Put your first number: "))
    usernum2 = int(input("Please put your second number: "))
    gcf = []
    minimum = min(usernum1, usernum2)
    for number in range(1, minimum+1):
        if usernum1 % number == 0 and usernum2 % number == 0:
           gcf.append(number)
    print(max(gcf))
        

findgcf() 
     


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
            




            
        
           
            
    
    
    
            




