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
x = Gen_Complex_Pass2(7)
