#The Big Books of Small Python Projects

#Project 1 - BAGELS
#April 9 2026

import random
import string

# For printing the result
# for beautifully print the result without any ''sign as general list element and also in one line not in muliple line
def print_result(list):
    if len(list)==3:
        a,b,c = list
        print(a,b,c)
    elif len(list)==2:
        a,b = list
        print(a,b)
    else:
        a = "" #make the a string first then concatenate the list element
        a += list[0]
        print(a)

def Bagels():
    secret_num = 134#random.randint(100,999) # getting a secret num of 3 digit using random.randit 
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
#Bagels()

#April 12 
#Project 2 - Birthday Paradox


def Birthday_Paradox():
    #first we'll generate a group of birthday e.g 33 people's birthday
    num_people = int(input("How many people's group you wanna test : ")) #the book uses 23 people group 
    
    match_found_count = 0

    for i in range(0,100000):
        
        count = num_people 
        birthday = []
        match_found = {}
        while(count > 0):            
            months  = ['January','February','March','April','May','June','July','August','September','October','November','December']
            dates = [j for j in range(1,32)] # 1,2,3,,,,31
            
            birthday_month = random.choice(months)
            if birthday_month == 'February': # Always Special care but couldn't consider leap year that might be too much !!!!!!
                dates = [j for j in range(1,29)]
                birthday_date = random.choice(dates)
            elif birthday_month == 'April' or birthday_month == 'June' or birthday_month == 'September' or birthday_month == 'November':
                birthday_date = random.randint(1,30) #used randint to randomly choosea date from 1 to 30
            else:
                birthday_date = random.choice(dates)

            birthday.append(str(birthday_date) + " " + birthday_month)
            count-=1
        for i in birthday:
            if i in match_found:
                match_found[i]+=1 #here the dictionary maybe unnecessay but i'm working with this problem for over hours so brain is not working now so i kept it
                match_found_count+=1
                break #here is something to tell actually the program wants to check if there's any match in the generated group of birthdays then count it as 1 
                    #that the birthday is matched they didn't tell to count how many matches are happening only count 1 if any matches and count 0 if there's no match
                    #earlier i was countine all matches and it's going far more that the expected answer then i paste my code to deepseek and ask to help 
                    #with my logical thinking error then i get to know about this and then fixed by myselft now the answer is matching with the book one
            else:
                match_found[i] = 1
    probability = (match_found_count/100000*100)
    print(f"The probability of found the same birthday among a group of  {num_people} people is : {probability}%") 
    #this program has a very logical and quite funny feature whereas 23 people's group has a 50% chances of matching the birthday 
    #but to get 100% matching you have to increase the people to 88 so this may have some logic and sense somehow 
    
#Birthday_Paradox()

#April 13 
#Project 3 - Bitmap Message
import re

def Bitmap_Message():
    print("Welcom To Bitmap Images by Mominur bin Mohammad Ratan Khan")
    #Drawing the bitmap manually with string
    bitmap2 = ' *                                     *\n' \
             ' *   *                             *   *\n' \
             ' *     *                         *     *\n' \
             ' *        *                   *        *\n' \
             ' *            *           *            *\n' \
             ' *                *   *                *\n' \
             ' *                  *                  *\n' \
             ' *                                     *\n' \
             ' *                                     *\n' \
             ' *                                     *\n' \
             ' *                                     *\n' 
    #Tryting to implement You'r Name sir (Dr. Tom Lotz). 
    bitmap =  " XXXXXX              XXXX            XX         XX\n"\
              " XXXXXX             XXXXXX           XX XX   XX XX\n"\
              "   XX              XXXXXXXX          XX  XX XX  XX\n"\
              "   XX              XXXXXXXX          XX    XX   XX\n"\
              "   XX               XXXXXX           XX         XX\n"\
              "   XX                XXXX            XX         XX\n" \
              

    #print(bitmap) # just to make sure everything is fine but only for debugging not for normal program or also can be shown to user as preview
    display = ''
    message = input("Enter your message : ")
    count = 0
    length_message = len(message)
    print(length_message)
    filter_message = ''
    #this for filtering the space from user message as it could break my program beauty by damaging the real bitmap sketch with space
    for i in message:
            if i == ' ':
                continue
            else:
                filter_message += i
    if len(filter_message) == 0: # if the user only entered space 
        print("Nothing it's just space entered you have to enter char,dig,something else space is just space in my program")
    else:
        for index,i in enumerate(bitmap):
            if i == 'X': #only deal with the 'X' , space will be just as space
                display += filter_message[count]
                count += 1
                if count >= len(filter_message): # again start from the starting of user text in filter message
                    count = 0
            else: #counting the spaces
                display += i

    print(display)
#Bitmap_Message()


#April 14


#calculating the score
def point_calc(list,owner):
    owner = 0 #always making the score 0 as it's gonna count through the whole list although i'm not sure about this tomorrow i'll check it 
    owner = int(owner)
    for i in list:
        if i[1] == 'K' or i[1] == 'Q' or i[1] == 'J':
            owner += 10
        elif i[1] == 'A':
            if owner + 10 > 21:
                owner += 1
            else:
                owner += 10
        else:
            (owner) += i[1]
    return owner

#judging the result basis on user and computer scores
def judge(computer_score,user_score):
    if (computer_score == user_score) and computer_score > 21:
        print("it's a tie")
    elif (computer_score > 21):
        print("computer burst")
    elif(user_score > 21):
        print("User burst and loose")
    elif((21-computer_score) > (21-user_score)):
        print("User wons  Gap with (21) ","user : ",(21-user_score) ,"vs","Computer : ",(21-computer_score))
    elif (computer_score == user_score):
        print("Tie")
    elif ((21-computer_score) < (21-user_score)):
        print('computer wons')
    return False


def BlackJack():
    print("Welcom to BlackJack By Mominur bin Mohammd Ratan")
    card_group = ['spade','club','heart','Diamond'] #groups of cards
    card_num = [2,3,4,5,6,7,8,9,10,'J','Q','K','A'] #13 cards in the box
    computer_score = 0  #initial score
    user_score = 0  #initial score
    computer_card = []  #dict for holding generated cards for computer
    for i in range(2): # generating 2 cards for computer
        computer_card.append([random.choice(card_group),random.choice(card_num)])    
    computer_score = point_calc(computer_card,computer_score) # calculating the score for computer


    #similar thing for user also
    user_card = [] 
    for i in range(2):
        user_card.append((random.choice(card_group),random.choice(card_num)))
    user_score = point_calc(user_card,user_score)

    #showing the computer's one card and user's both card to user
    print(f"Computer's 1st card : {computer_card[0]}")
    print(f"User Card : {user_card} User's Score ; {user_score}" )

    flag = True #loop controller

    while(flag):
        choice = input("Stand (s) Hit (h)").lower() # stands for bid and hit for taking another card and adding it's score
        if choice == 's':
            flag = judge(computer_score=computer_score,user_score=user_score)
        else:
            user_card.append((random.choice(card_group),random.choice(card_num)))
            user_score = point_calc(user_card,owner=user_score)
            print(f"User Card {user_card}, user Score {user_score} ")
            if user_score > 21:
                flag = judge(computer_score=computer_score,user_score=user_score)
            else:
                None



    print(f"Computer card : {computer_card} Computer_Score  : {computer_score}")
    print(f"User card : {user_card} user Score : {user_score}")
BlackJack()