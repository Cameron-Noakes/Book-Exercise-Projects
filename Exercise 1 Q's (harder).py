import time
import random
#Exercise 1:

# Q1. Write a program to accept a student name, and the marks obtained on 10-weekly tests,
# Print the name, average mark, top three marks and bottom three marks.
# Use 'sortedMarks = sorted(markList, reverse = True)'

# Q2. From the table, find the months with the hottest average temperature and the coldest
# average temperature, print the month names with the temperatures of these months.

# Q3. Simulate how the top scores of several players playing an online game many times could
# be held in a list.

# Q3a: Define a 2D list which will hold in each row, a userID and their
# top score for an online game. The list shoud be initialised with the values used in Q3a.

# Q3b. Ask a user to enter their ID. Check if the user is in the list. If it is not append
# a new row containing their userID and a score of zero.

#Q3c. Generate a random number between 50 and 200 to represent the score for this game.
# Locate the user, check whether the new score is > than current and if so replace it.



#Question 1.

list01 = []
studentname = input("\nEnter Student name: ")
x = 0
for y in range (1,11):
    
    markList = int(input("Enter marks for test of " + studentname + ": "))
    list01.append(markList)
    x = int(markList) + x
    if x == 10:
        break

avg = x/10

#---------------------------------------------------------------------------------------------------------------------#
#Use 'sortedmarks = sorted(markList, reverse = True)'                                                                 ¦
#key=int used and markList is appended to list01 so essentially,                                                      ¦
#'sortedmarks = sorted(markList, reverse = True)' == 'sortedmarks2 = sorted(list01, key=int, reverse = True)'         ¦
#---------------------------------------------------------------------------------------------------------------------#

sortedmarks = sorted(list01, key=int) #Ascending
sortedmarks2 = sorted(list01, key=int, reverse = True) #Descending

print (studentname, "\t Average is:", avg, "\t","\nTop 3 Marks:\tBottom 3 Marks:")

print(sortedmarks.pop(-1),'            ',sortedmarks2.pop(-1))
print(sortedmarks.pop(-1),'            ',sortedmarks2.pop(-1))
print(sortedmarks.pop(-1),'            ',sortedmarks2.pop(-1))
print ("Q4 is now 3..2..1")
time.sleep(3) # Organised Delay

#Question 2.

#Table Data.
Months = [  ["January",6,3],
            ["February",7,3],
            ["March",10,4],
            ["April",13,6],
            ["May",17,9],
            ["June",20,12],
            ["July",22,14],
            ["August",21,14],
            ["September",19,12],
            ["October",14,9],
            ["November",10,6],
            ["December",7,3],
            ]

data = input("Load Sorted Months?: ")
print ("  Month,   Hot,  Cold")

print ("\n",Months[6],"\n",Months[7],"\n",Months[5],"\n",Months[8],"\n",Months[4],"\n",Months[9],"\n",
       Months[3],"\n",Months[2],"\n",Months[10],"\n",Months[1],"\n",Months[11],"\n",Months[0],"\n")

#Question 3.

player = [  [" AAA01",135],
            ["BBB01",87],
            ["CCC01",188],
            ["DDD01",109],
            ]
#Question 3b.

User1 = input("Enter UserID: ")

if User1 == "AAA01" or User1 == "BBB01" or User1 == "CCC01" or User1 == "DDD01":
    print ("UserID already in Database.\n")
    print ("  userID   topScore")
    print (player[0],"\n",player[1],"\n",player[2],"\n",player[3])
 
elif len(User1) != (5):
    print ("Invalid userID.")

else:
    player.append([User1])
    player[4].append(0)
    print ("  userID   topScore")
    print (player[0],"\n",player[1],"\n",player[2],"\n",player[3],"\n",player[4])

#Question 3c. and Question 3d.

score = random.randint(50,200)
print ("\nNew Score is:",score,"for",User1,"\n")

#Over Values:

if User1 == "AAA01":
    if score > 135:
        player[0].remove(135)
        player[0].insert(1,score)
        print (player[0],"\n",player[1],"\n",player[2],"\n",player[3])

elif User1 == "BBB01":
    if score > 87:
        player[1].remove(87)
        player[1].insert(1,score)
        print (player[0],"\n",player[1],"\n",player[2],"\n",player[3])
        

elif User1 == "CCC01":
    if score > 188:
        player[2].remove(188)
        player[2].insert(1,score)
        print (player[0],"\n",player[1],"\n",player[2],"\n",player[3])

elif User1 == "DDD01":
    if score > 109:
        player[3].remove(109)
        player[3].insert(1,score)
        print (player[0],"\n",player[1],"\n",player[2],"\n",player[3])
        
        

            
#Under Values continue program. Over Values replace current Value and prints.
#If a 'syntax error' occurs just rerun the script.

time.sleep(3) #Organised Delay

