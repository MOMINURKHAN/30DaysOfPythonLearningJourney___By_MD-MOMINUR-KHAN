import math
#define a func to add two Number
def Add_Number(num1,num2):
    return num1 + num2

#define a func to calculate area of a circle
def area_of_Circle(radius):
    return math.pi*radius**2

#define a func to add arbitrary number of argument
def add_arbitrary(*args):
    print(type(args[0]))
    sum = 0
    for i in args:
        if isinstance(i,int):
            sum=sum+i
            #print(f" I : {i}, sum  : {sum}")#it was to check how it's working
        else:
            print(f"'{i}' It's not a valid type, Enter Integer Please")
            return
    
    return sum

#def a func to calc factorial
def calc_factorial(num_n):
    factorial = 1
    for i in range(1,num_n+1):
        factorial = factorial * i 
    return factorial

#def a  func to verify if the parameter is /is not empty
def is_empty(argument):
    if not argument:
        print("It's an empty parameter passed this time")
    else:
        print("it's not empty it has {}".format(type(argument)))


import statistics
#this one is using built in func
def check_median1(lst):
    return statistics.median(lst)


#this one is using logic
#after several month I sort a list using loop feels good 11.30.2025
def sort_list(lst): #sorting from lower to upper
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]>lst[j]:
                x = lst[i]
                lst[i] = lst[j]
                lst[j] = x
            else:
                None

    print(lst)
    return lst

def check_median2(lst):
    lst = sort_list(lst=lst)
    if len(lst)==0:
        print("there's no element in the list")
        return None
    elif len(lst)%2==0:
        return (lst[int((len(lst))//2)] + lst[(int(len(lst)/2))-1])/2
    else:
        return lst[int(len(lst)/2)]


        


age = [3,34,23,6,43,55,18,23,53,23,53,34,64,65,786,786,335]
print(age)

print("Median Value : ",check_median2(age))

def calculate_mode(lst):
    #***Find the most frequent element in a list ***
    lst = sort_list(lst=lst)# sort input list
    unique_item = set(lst) #get unique element
    Dictionary = {} 
    for items in unique_item: #run the loops in the set (which contains unique elements)
        Dictionary[items] = lst.count(items) #updating dictionary with unique elements as keys and count/appearance as values
    
    print(Dictionary.items())#just for check if everything going smoothly
    #here the max value and target key is for finding the max value(appearance/count of a single key in the dictionary) and the corresponding keys
    max_value = 0
    target_key = None
    for key,value in Dictionary.items():
        if value > max_value:
            max_value = value
            target_key = key
    print("This is the item with most frequency : ",target_key)
    

#took around 2.5 to 3 hours to understand and implement fully 
#lots of time and mental stress but feeling good
#understand : tuple,dictionary ,list,set's some methods and property's
#worked with sorted and lambda and enumerate good good
def calculate_mode_top_N(lst,n):
    lst = sort_list(lst=lst)
    unique_itemps = set(lst)
    Frequency = {}
    for item in unique_itemps:
        Frequency[item] = lst.count(item)
    print(Frequency)

    sorted_frequency = dict(sorted(Frequency.items(), key=lambda item : item[1],reverse=True))
    sorted_items = sorted(sorted_frequency.items(), key=lambda x:x[1],reverse=True)
    top_5_items = sorted_items[0:n]
    top_items_dic = dict(top_5_items)
    
    for i,(key,value) in enumerate(top_items_dic.items()):
        print(f" ranking : {i} \t : the item : {key} \t Appearance : {value}")  

calculate_mode_top_N(age,4)

def calculate_range(lst):
    lst = sort_list(lst)
    range = lst[len(lst)-1] - lst[0]
    print("Range : ",range)
    return range
calculate_range(age)