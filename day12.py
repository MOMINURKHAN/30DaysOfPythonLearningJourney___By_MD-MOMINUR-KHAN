import string
import random


def Gen_Pass(num): #Generate Weak Password
    password = []
    print("String Password : 1 \
          Numeric Password : 2 \
          Punctuation Password : 3")
    try:
        choice = int(input("Enter your choice : "))
        for i in range(0,num):
            if choice == 1:
                password.append(random.choice(string.ascii_letters))
            elif choice == 2:
                password.append(random.choice(string.digits))
            elif choice==3:
                password.append(random.choice(string.punctuation))  
            else:
                print("invalid Input Please enter according the displayed message")
                return None
        
        x = "".join(password)
        print("Easy Password (Gen_Pass) : ", x)
        return x
    except ValueError():
        print("Enter a valid Choice")

def Gen_Complex_Pass(length):#My try
    while length<8:
        length = int(input("Length Must > 8 (Enter Again):"))
    password = []
    Alphabet = string.ascii_lowercase + string.ascii_uppercase
    Digit  = string.digits
    Punctuation = string.punctuation
    print("Enter your chioce what you want to include in your password : ")
    print("e.g.1 -Alpha . 2 - Digit,  12/21 - (Alpha.. + Dig..) or 123/321/132(Alpha + DIg.. + Punc) or 13 (Alpha + Punct)...: ")
    print("Alphabet = 1 " \
          "Digit    = 2 " \
          "Punctuation = 3 ")
    try:
        choice = int(input("Enter your choice : "))
        for i in range(length):
            match choice:
                case 1:
                    password.append(random.choice(Alphabet))
                case 2:
                    password.append(random.choice(Digit))
                case 3:
                    password.append(random.choice(Digit))
                case 12 | 21:
                    temp = Alphabet + Digit
                    password.append(random.choice(temp))
                case 13 | 31:
                    temp = Alphabet + Punctuation
                    password.append(random.choice(temp))
                case 23 | 32:
                    temp = Digit + Punctuation
                    password.append(random.choice(temp))
                case 123 | 321 | 132 | 213 | 231| 312:
                    temp =Alphabet + Digit + Punctuation 
                    password.append(random.choice(temp))
                case _:
                    print("Wrong Chioce Enter it correctly Next time")
                    return None
    except ValueError:
        print("Please Enter Valid Digit from Displayed Instruction ")
    display = "".join(password)
    print(display)
    return display

def Gen_Complex_Pass2(length):#optimesed way from GFG-GeeksForGeeks
    
    Alphabet_low = list(string.ascii_lowercase)
    Alphabet_Upp = list(string.ascii_uppercase)
    Digit = list(string.digits)
    Symbol = list(string.punctuation)
    password = [] #List Password
    while length<8:
        try:
            length = int(input("Enter length Again  length> 8:  "))
        except ValueError:
            print("Enter a valid Length of your desire Password ")

    #we'll take 60% -> letter and 40% -> digit + Special Characters
    part1 = round(length*(30/100))
    part2 = round(length*(20/100))

    random.shuffle(Alphabet_low) 
    random.shuffle(Alphabet_Upp) 
    random.shuffle(Digit)
    random.shuffle(Symbol)

    for i in range (part1):
        password.append(Alphabet_low[0])
        password.append(Alphabet_Upp[0])
    for i in range(part2):
        password.append(Digit[0])
        password.append(Symbol[0])
    
    random.shuffle(password)
    x = "".join(password)
    print("Your Password : {}".format(x))
    return x

#Rge Color Gen 1.iii
def Rgb_Colr_Gen(): #Number -> How many
    Rgb_Colour = []
    for i in range(0,3):
        Rgb_Colour.append(random.randint(0,255))
    
    #print(tuple(Rgb_Colour))
    return Rgb_Colour
    
#2.ii
def list_rgb_color(number):#num -> how many colour needed
    num_lst = []
    for i in range(0,number):
        x = Rgb_Colr_Gen()
        num_lst.append(x)

    
    return num_lst

def hexacolgen():
    base = ["a","b","c","d",'e','e',0,1,2,3,4,5,6,7,8,9]
    hexaCol = ['#']
    random.shuffle(base)
    for i in range(6):
            hexaCol.append(str(base[i]))#convert to string while appending otherwise later .join is not helping to print
    
    print("".join(hexaCol))
    return hexaCol
#x = hexacolgen()
#it's just to remember the enumerate function's uses
def display(x):
    for i,(c1,c2,c3) in enumerate(x,1):
        print(f"index : {i} color(rgb) : {c1},{c2},{c3}")

#3.i
#import age from day11 and apply shuffle
from day11 import age 
def shuffle_list(lst):
    return random.shuffle(lst)

# shuffle_list(age)
# print(age)

def random_number(length,max_num = 9):
    if length>max_num:
        raise ValueError(f"{length} can't be more than {max_num}")

    random_array = []
    while len(random_array)<length:
        random_element = random.randint(0,9)
        if random_element not in random_array:
            random_array.append(random_element)
        
    return random_array

random_number(8)

#maybe if i had more time i would try 
