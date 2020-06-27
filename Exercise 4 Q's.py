
#Exercise 4 Questions:

#Tip: Comment out sections that you wish to not test.

#Q1. write a program to generate 10 random
# numbers between 1 and 10 and print out
# the 10 numbers and the total of them all.

#Q2. Extend the program in Q1 to repeat the
# generation of 10 random numbers 1000 times,
# Do not print out the numbers or the total ,
# just the average of th etotals at the end.

#Q3. Write a program to allow a user to input
# a number of 5-character product codes, beginning
# with the letters "AB"or "AS" followed by 3 numbers.
# Count and print the total number of codes starting
# with "AB" and the total of product codes ending in 00.
#
# Test by inputting: AS123,AS101,AB111,AB345,CD222,AB200.
import random
import time

#Question 1.

y = 0
for x in range(0,10):
    random_no = random.randint(0,11)
    print (random_no)
    y = random_no + y
    

print ("Total of random numbers: ",y)
print ("Q2 is now 3..2..1")
time.sleep(3) #Delay of 3

#Question 2.

y = 0
for x in range (1000):
    for x in range(0,10):
        random_no = random.randint(0,11)
        y = random_no + y
        break

print ("the average total is: ",y/1000)
print ("Q3 is now 3..2..1")
time.sleep(3) #Delay of 3

#Question 3.
ab = 0
zero = 0
procode = 0
while procode != -1:
    procode = input ("(-1 to stop) Input product codes: ")

    if procode == -1:
        break
    
    if procode.startswith("AS"):
        print (procode)
    

    if procode.startswith("AB") and len(procode)== 5:
        ab = ab +1
        print ("AB counter:",ab)

    if procode.endswith("00") and len(procode) == 5:
        zero = zero +1
        print ("Ending zeros =",zero)
    
    if len(procode) >=6:
        print ("To many characters")

    if len(procode) <5:
        print ("To little characters\n")


    if procode == "-1":
        break

print ("Total AB codes:", ab, "\nTotal ending 00 codes:",zero)


    

    


        


