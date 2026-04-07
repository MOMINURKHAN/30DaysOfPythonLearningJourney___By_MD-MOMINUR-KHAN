#from Jenny Maam's python playlist

#******Project 1

#make a password generator using the random module
import random as ran
import string
def password_generator():

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

import requests
import re
def hangman_game():
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
        



                
