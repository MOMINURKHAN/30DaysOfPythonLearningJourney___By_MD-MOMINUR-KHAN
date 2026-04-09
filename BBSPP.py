#The Big Books of Small Python Projects

#Project 1 - BAGELS
#April 9 2026

import random
import string

# For printing the result
# for beautifully print the result without any ''sign as general list element and also in one line not in muliple line
def print_result(list):
    if len(output)==3:
        a,b,c = output
        print(a,b,c)
    elif len(output)==2:
        a,b = output
        print(a,b)
    else:
        a = "" #make the a string first then concatenate the list element
        a += output[0]
        print(a)

secret_num = random.randint(100,999) # getting a secret num of 3 digit using random.randit 
secret_num_str = str(secret_num) # converting it to string to easily covert to list
secret_num_lst = list(secret_num_str) # now it's converting to list
print(secret_num,secret_num_str,secret_num_lst) 
flag = 10 #user have this much chances to guess
while(flag > 0):
    output = [] #store the match/non-match/match but index wrong all these stuff with 'fermi','pico','bagels'
    flag -= 1
    guess_num = input(f"Guess #{10-flag} : \n> ") # taking user input in a beautiful way
    loop_checker = 0 #to check if the guessed number is fully matching with the software generated number e.g fermi,fermi,fermi then stop the program
    for index,i in enumerate(guess_num): # index and i 
        for sec_index,j in enumerate(secret_num_lst): # second index = sec_index and j 
            print(i,j,index,sec_index)
            if i == j: # if number match then also check the index in the nested if
                
                if  index == sec_index:
                    output.append('Fermi')
                    loop_checker += 1
                    break      
                else:
                    output.append('Pico')
                    break
    
    if len(output) == 0: # nothing matches -> Bagels
         output.append('Bagels')
    print_result(output) # calling the 'print_result' function for showing output
    
    if loop_checker >= 3: #['fermi','fermi','fermi']
        print(f"You Won , you successfully guessed it : {secret_num}")
        decision = input("You want to play more - yes otherwise no").lower()#if user wants to play more
        if decision == 'yes':
            flag = 10
        else:
            flag = 0
    if flag==1:
        print(f"You loose. The number was {secret_num}")
        decision = input("You want to play more - yes otherwise no").lower()#if user wants to play more
        if decision == 'yes':
            flag = 10
        else:
            flag = 0

                     
#there's still a problem left with this program it can't get the repetitive number #
# eg. 111 or 122 or 331 anything it'll make mistake i'll work later it's already 21.29 i need to pack up 
            
