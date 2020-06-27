import time
import random
#Exercise 5:

#Q1. define an empty list (alist) and append 'apple' to it,
# then define another (blist) filled with 20 integer elements of zero,
# concatenate alist and blist into 'clist', then remove the last element
# of clist and save in variable 'lastC'.

#Q2. Initialise an empty list, ask the user to enter as many names as they like,
# until they enter 'End'. Slice the list in half and print the first half of the
# list. If the list is odd, just print the first four elements.


#Question 1a.
alist = []

alist.append("apple")

blist = ["0," * 20]

clist = alist + blist

lastC = clist.pop()

print ("Q2 is now 3..2..1")



#Question 2.
list1 = []
name = (" ")

while name != "End":
    name = input("Input as many names as you'd like: ")
    list1.append(name)
    
    
    
    if name == "End":
        list1.remove("End")
        break
    

print (list1)
number =(len(list1))

no_of_names = (number)
print (no_of_names)
listodd = list1[0:4] # Starting at 1 up by 2 
listeven = list1[::2] # Starting at 0 up by 2


if number %2 == 0:
    print ("Even:",listeven) # If even print half

    

if number %2 == 1:
    print ("Odd:",listodd)# If odd print 1st 4 items






