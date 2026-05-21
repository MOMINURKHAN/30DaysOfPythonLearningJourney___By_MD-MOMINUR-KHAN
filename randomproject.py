#from Jenny Maam's python playlist

#******Project 1

#make a password generator using the random module

def password_generator():
    import random as ran
    import string
    letter = []
    for ch in string.ascii_letters:
        letter += ch
    digit = []
    for dig in string.digits:
        digit.append(dig)
    symbol = []
    for sym in string.punctuation:
        symbol+=sym

    print(symbol)
    #How many letter,digit and symbol the user wants
    n_letters = int(input("How many letters you want ?"))# e.g : 1,2,7,8,n....
    n_digit = int(input("how many digit you want"))
    n_symbol = int(input("how many symbol you want ? "))
    password = []

    for i in range(0,n_letters): # 0,1,2,...n_letters
        password+=ran.choice(letter)
    for i in range(0,n_digit):
        password+=ran.choice(digit)
    for i in range(0,n_symbol):
        password+=ran.choice(symbol)

    print(password)
    password_str=""
    ran.shuffle(password)
    for i in password:
        password_str+=i
    print(password_str)



#project 2

#Hangman Game - kind of word guessing game with some rules and system - later if i forgot just need to search online hangman game to remember

#we need something to generate random word first so we'll go with website scraping and using the resourches of that scraped website

def hangman_game():
    import requests
    import re
    import random as ran
    response = requests.get('https://www.mit.edu/~ecprice/wordlist.10000')

    words = response.content.decode('utf-8').splitlines()

    hangman_word = ran.choice(words)
    hangman_word_list = list(hangman_word)


    original_word = ['_' for i in range(0,len(hangman_word))]


    hangman_body = ['''
            +---+
            
            |   |
            0   |
                |
                |   
                |
            =========
                                                                                                    
            ''','''
            +---+
            
            |   |
            0   |
           /    |
                |   
                |
            =========
            ''','''
            +---+
            
            |   |
            0   |
           / \  |
                |   
                |
            =========
            ''','''
            +---+
            
            |   |
            0   |
           /|\  |
                |   
                |
            =========
            ''','''
            +---+
            
            |   |
            0   |
           /|\  |
           /    |   
                |
            =========
            ''','''
            +---+
            
            |   |
            0   |
           /|\  |
           / \  |   
                |
            =========
            ''']

    live = 6
    count = 0 #this for counting the original number
    flag = False

    while not flag:
        print(f"word : {original_word}")
        word = input("Enter a word : ")
        if word in original_word:
            live-=1
            print(f"You have repeated the same word that's already taken You have {live} left ")
            if live==0:
                flag = True
            
        if word in hangman_word_list:
            count+=1
            for index,i in enumerate(hangman_word_list):
                if i==word:
                    original_word[index] = word
                    #print(original_word)
                    if original_word==hangman_word_list:
                        print("You won the game ")
                        print(f"you got it : {hangman_word}")
                        flag = True
                        break;
            if flag:
                break
        else:
            live-=1
            print(hangman_body[6-live-1])
            print(f"you have {live} live left")
            
            if live==0:
                print("You loose")
                print(hangman_word)
                break;


def Ceaser_Cipher():# a tool to encrypt or decrypt texts(a-z,A-Z) it can also encrypt/de.. the digits but i didn't add here that thing just simple texts encription
    import string
    mode  = input("Wanna Encrypt or Decrypt ? E/D")
    print(mode)
    if mode == 'E' or mode == 'e':
        print("Encryption of given texts")
        letters = string.ascii_lowercase
        letter = list(letters)
        user_text = input("Write your message here : ").casefold()
        secret_code = int(input("write your secret code here : "))
        en_text = '' # Encrypted Text
        for i in range(len(user_text)):
            for index,j in enumerate(letter):
                if user_text[i]==j:
                    calculated_index = ((index+secret_code)%len(letter))
                    en_text+=letter[calculated_index]
                    break
            else:
                if user_text[i]==' ':
                    en_text+=' '
                else:
                    en_text+=user_text[i]
                    continue

        print(en_text)
    else:
        print("Decription of Text")
        letters = string.ascii_lowercase
        letter = list(letters)
        user_text =input("Enter message : ").casefold()#"Gur dhvpx".casefold() # oebja sbk whzcf bire gur ynml qbt, gura fgnlf naq cynl sbe n juvyr"
        secret_code = int(input("Enter secret code : "))
        de_text = '' # decrypted Text   
        for i in range(len(user_text)):
            for index,j in enumerate(letter):
                if user_text[i]==j:
                    calculated_index = ((index-secret_code)%len(letter))
                    if calculated_index<0:
                        calculated_index+=26
                    de_text+=letter[calculated_index]
                    break
            else:
                if user_text[i]==' ':
                    de_text+=' '
                else:
                    de_text+=user_text[i]
        print(user_text)
        print(de_text)

#8 April 2026

#project 5 of jenny ma'am
#Silent Aution program
#it's kind of project bidding and the final good bid will win 
def Silent_Auction1():
    print("This is Silent Auction Program (with list - method 1 by me)- Project 5 Jenny Ma'am")
    import os
    highest_bid = 0
    bid_info = []
    name_bidder = []
    i = True
    while(i):
        name =  input("Write your name : ")
        bid = int(input("Enter your bid : "))
        bid_info.append(bid)
        name_bidder.append(name)
        ask = input("Are there any other bidder or stop : yes or no \t")
        print(name_bidder)
        if ask == 'no':
            i = False
        else:
            os.system('clear')
        


    for index,i in enumerate(bid_info):
        if i>highest_bid:
            highest_bid = i
            winner = name_bidder[index]
        

    print(f"Highest bid is : {highest_bid},\nWinner is : {winner}")
    #programme finished here


import os


#function to check calculate the winner based on the highest bid
def check_winner(dict):
    current_price = 0
    highest_price = 0
    winner_name = ''
    for i in dict:
        current_price = dict[i]
        if current_price>highest_price:
            highest_price = current_price
            winner_name = i
    print(f"winner : {winner_name} highest Bid : {highest_price}")
    bidder_info = {}
    flag = False
    while(not flag):
        name = input("Enter your name : ")
        price = int(input("Enter your bid : "))
        bidder_info[name]=price

        ask = input("if more bidder : yes otherwise no").lower()
        os.system('clear') # to clear the screen and hiding the previous bidder info
        if ask=='no':
            flag = True
            check_winner(bidder_info)
def silent_auction2():
    bidder_info = {}
    flag = False
    while(not flag):
        name = input("Enter your name : ")
        price = int(input("Enter your bid : "))
        bidder_info[name]=price

        ask = input("if more bidder : yes otherwise no").lower()
        os.system('clear') # to clear the screen and hiding the previous bidder info
        if ask=='no':
            flag = True
            check_winner(bidder_info)


#20 Apr 2026
#jenny ma'am project 6
#Building simple calculator

def calculator():
    print("Welcome to simple Calculator made by Mominur bin Mohammad Ranta")
    user_operation = input('Which operation you wanna operate : (+,-,/,*,%)')
    sign = ['+',"*"]
    m = 100
    n = 200
    i,j = sign
    print(m * n)
calculator()

#from Dr Tom's/Teacher Tom's Python Corner
#8 April 2026

def explore_pi():
    import math
    import random
    L_needle = 5
    distance = 10
    Number_of_contact = 0

    for drops_count in range(0,10000000):
        alpha = random.uniform(0,90) # the angle between the dropped needle with lines
        x = random.uniform(0,distance/2) #the distance of needle center from the lines
        alpha_red = math.radians(alpha)
        sine_value = math.sin(alpha_red)
        if x<= ((L_needle*sine_value)/2):
            Number_of_contact+=1
    

    pi = ((2*L_needle*drops_count))/(distance*Number_of_contact)
    print(pi)
def birthday_match():
    import random
    index = 0
    match_dict = {'birthday':'number'}
    temp_list = []
    for i in range(0,10000):
        First_age = random.randint(0,365)
        print(First_age)
        while(1):
            index+=1
            second_age = random.randint(0,365)
            print(First_age,second_age)
            if First_age==second_age:
                temp_list.append(index)
                index=0
                break;
    print(temp_list)
    sum = 0
    average = 0
    for i in temp_list:
        sum+=i
    average = sum/10000
    print(average)























#it's a math graph displaying by doubao AI
def math_graph():
    import numpy as np
    import matplotlib.pyplot as plt

    # Create figure with 2x2 subplots
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Systems of Linear Equations', fontsize=16)

    # -------------------------- (a) --------------------------
    x = np.linspace(-1, 5, 100)
    y1_a = 4 - x
    y2_a = x - 2
    axs[0,0].plot(x, y1_a, label=r'$x_1 + x_2 = 4$', color='blue')
    axs[0,0].plot(x, y2_a, label=r'$x_1 - x_2 = 2$', color='red')
    axs[0,0].scatter(3, 1, color='black', zorder=5, label='Intersection (3,1)')
    axs[0,0].set_title('(a) 1 Solution')
    axs[0,0].grid(True)
    axs[0,0].legend()
    axs[0,0].axhline(0, color='black', linewidth=0.5)
    axs[0,0].axvline(0, color='black', linewidth=0.5)

    # -------------------------- (b) --------------------------
    x = np.linspace(-3, 5, 100)
    y1_b = (4 - x)/2
    y2_b = (-4 - 2*x)/(-4)  # Simplifies to (-2 - x)/2
    axs[0,1].plot(x, y1_b, label=r'$x_1 + 2x_2 = 4$', color='blue')
    axs[0,1].plot(x, y2_b, label=r'$-2x_1 - 4x_2 = 4$', color='red')
    axs[0,1].set_title('(b) 0 Solutions (Parallel)')
    axs[0,1].grid(True)
    axs[0,1].legend()
    axs[0,1].axhline(0, color='black', linewidth=0.5)
    axs[0,1].axvline(0, color='black', linewidth=0.5)

    # -------------------------- (c) --------------------------
    x = np.linspace(-1, 3, 100)
    y1_c = 2*x - 3
    y2_c = (-6 + 4*x)/2  # Simplifies to 2x - 3
    axs[1,0].plot(x, y1_c, label=r'$2x_1 - x_2 = 3$', color='blue', linewidth=3)
    axs[1,0].plot(x, y2_c, label=r'$-4x_1 + 2x_2 = -6$', color='red', linestyle='--', linewidth=2)
    axs[1,0].set_title('(c) Infinitely Many Solutions (Coincident)')
    axs[1,0].grid(True)
    axs[1,0].legend()
    axs[1,0].axhline(0, color='black', linewidth=0.5)
    axs[1,0].axvline(0, color='black', linewidth=0.5)

    # -------------------------- (d) --------------------------
    x = np.linspace(-1, 4, 100)
    y1_d = 1 - x
    y2_d = x - 1
    y3_d = (3 + x)/3
    axs[1,1].plot(x, y1_d, label=r'$x_1 + x_2 = 1$', color='blue')
    axs[1,1].plot(x, y2_d, label=r'$x_1 - x_2 = 1$', color='red')
    axs[1,1].plot(x, y3_d, label=r'$-x_1 + 3x_2 = 3$', color='green')
    axs[1,1].scatter(1, 0, color='black', zorder=5, label='Intersection of 1&2')
    axs[1,1].scatter(0, 1, color='purple', zorder=5, label='Intersection of 1&3')
    axs[1,1].scatter(3, 2, color='orange', zorder=5, label='Intersection of 2&3')
    axs[1,1].set_title('(d) 0 Solutions (No Common Intersection)')
    axs[1,1].grid(True)
    axs[1,1].legend()
    axs[1,1].axhline(0, color='black', linewidth=0.5)
    axs[1,1].axvline(0, color='black', linewidth=0.5)

    plt.tight_layout()
    plt.show()



            
