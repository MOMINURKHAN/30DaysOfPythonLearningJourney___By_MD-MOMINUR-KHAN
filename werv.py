#we'rv = weekly review of learned stuffs

#from day18.py 
#what i remember is ; i learned the regular expression modules some function
#findall - to find all the matches

#project 1 - password generator - jenny ma'am python series project 2

import random
import string
print("Hello world")
def password_generator():
    print("''''Welcome to the Password Generator By  MOMINUR BIN MOHAMMAD RATAN KHAN")
    print("Simple Password generator i haven't added the complex design or structure to make some hyper complex" \
    "password rather than it's simple and user friendly  how the user want can make his own password" \
    "with enough strength and char+digit+spec_char mix up ")
    character = string.ascii_letters
    digit = string.digits
    special_char = string.punctuation

    flag = False
    while(not flag):
        print("Enter the password configuration how many digit/char/special char you want")
        num_char = int(input("how many character you want ? "))
        num_dig = int(input("how many digit you want "))
        num_spec_char = int(input("how many special char you want "))
        password = []
        for i in range(0,num_char):
            password+=random.choice(character)
        for i in range(0,num_dig):
            password+=random.choice(digit)
        for i in range(0,num_spec_char):
            password+=random.choice(special_char)
        
        random.shuffle(password) #shuffle to mix the password's digit,char & spec_char together
        password_str = '' # converting password list to a password string for easy and right exhivision to user
        for i in range(len(password)):
            password_str+=password[i]
        print(f"Password Generated Successfully : {password_str}")
        program_running = input("Do you want to make another one (yes/no) :- ")#if the user want to make more password
        if program_running == 'yes':
            continue
        else:
            flag = True

# password_generator()

#project 2 - hangman Game - Jenny ma'am's python course project 3 

import requests
def hangman_game():
    print("Welcome to the Hangman Game by MOMINUR BIN MD RATAN KHAN")
    print(""" Welcome to Hangman Game Here the computer will generate a random word and you've to guess the word by character if you 
          guess the wrong character you'll lose one life in total you'll have 6 live and it'll gradually draw a hangman also 
          so give it a try. 
    """)
    #using request.get function we scrap the following mit website for getting 10000 english words 
    response = requests.get('https://www.mit.edu/~ecprice/wordlist.10000')
    words = response.content.decode('utf-8').splitlines()
    selected_word = random.choice(words) # select a word from 10000 words
    word_length = len(selected_word)
    display_list = ['-' for i in range(word_length)]
    count = 0
    live = 6
    print(display_list)
    while(live > 0):
        user_guess = input("Guess a character \n>")
        if user_guess not in selected_word:
            live-=1
            print(f"you have {live} left")
            hangman_visualise(5-live)
            if live==0:
                print(f"you've failed the word was {selected_word}")
            
        else:
            for index,i in enumerate(selected_word):
                if user_guess == i:
                    display_list[index] = i
                    print(display_list)
                    count+=1
            if count==word_length-1:
                print(f"You've got this {selected_word}")
#it's a part of hangman Game where it show a person is hanging gradually based on the user's wrong guess    
def hangman_visualise(int):
    hangman_sketch = ["""
         ----       |                
          |         |
          0         |
                    |
                    |
                    |
                    |
                    |
        ""","""
         ----       |                
          |         |
          0         |
         /          |
                    |
                    |
                    |
                    |
        ""","""
         ----       |                
          |         |
          0         |
         / \        |
                    |
                    |
                    |
                    |
    
    ""","""
    
         ----       |                
          |         |
          0         |
         /|\        |
                    |
                    |
                    |
                    |
        ""","""
         ----       |                
          |         |
          0         |
         /|\        |
         /          |
                    |
                    |
                    |
        ""","""
         ----       |                
          |         |
          0         |
         /|\        |
         / \        |
                    |
                    |
                    |
        """]
    print(hangman_sketch[int])

#hangman_game()

#project 3 - Ceaser Cipher by Jenny Ma'am's python course project 4 
def Ceaser_Cipher():
    print("Welcome to Ceaser_Cipher by Mominul bin Mohammad Ratan Khan")
    print("The Ceaser_cipher is a technique to encode the text/digit anything with some secret code" \
    "the other person/computer need the exact secret code to decode the encoded thing")
    flag = True
    while(flag):
        user_choice = input("Want to Encode or Decode(E/D)").lower()#if wanna encode or decode
        words = string.ascii_lowercase #contains a-z in lowercase 
        if user_choice == 'e':
            user_text = input("Enter The Text : ").lower()
            secret_code = int(input("Enter the Secret Code : "))
            encoded = ''
            for i in user_text:
                if i in words:
                    for index,j in enumerate(words):
                        if i ==j :
                            encoded += words[(index+secret_code )% 26]
                else:
                    encoded+=i
            print(encoded)
        else:
            user_text = input("Enter The Text : ").lower()
            secret_code = int(input("Enter the Secret Code : "))
            decoded = ''
            for i in user_text:
                if i in words:
                    for index,j in enumerate(words):
                        if i==j:
                            index_calculation = (index-secret_code)
                            if index_calculation < 0:
                                index_calculation += 26
                            decoded += words[index_calculation%26] 
                else:
                    decoded += i
            print(decoded)
            
                
#Ceaser_Cipher()

#project 4 - Needle drop test to get approximate Pie value by Teacher Tom - Python Corner

def Needle_Pie():
    print("Welcome to Needle Pie Test by Mominur Bin  Ratan Khan")
    print("So basically we'll take a fixed size of paper with vertical lines drawing on them the gap between two vertical line is d " \
    "then we'll have a needle of l cm/length so we'll drop the needle from a fixe distance to the paper and we'll count how many times" \
    "it touches the vertical lines then with some formula we'll calculate the pie value - it's a fun one if we try in real life just imagine" \
    "working on lab for months dropping needle on the paper for million time hahahah")
    

#i Actually forgot this problem's equations so i'll ask teacher tomorrow maybe cz today is sunday he should be busy
# but i'll come back buddy even forget what about weekend review that time i'll see you 


