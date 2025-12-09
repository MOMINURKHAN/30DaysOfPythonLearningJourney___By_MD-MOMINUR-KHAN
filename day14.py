#there are just playing with the examples
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable
#to fileter short name i mean to take short name and clear long ones 
x = filter(lambda n:len(n)<7,names)
#we can also use the logical operator here 
#x = filter(lambda n:n if len(n)<7 else False,names)
#while printing the filtered , mapped we need to convert the variable into list( or any other iterable ) first then we can show them

from functools import reduce
#try implementation of reduce function with lambda to add the all names together in the list names
x = reduce(lambda a,b:a.upper()+" "+b.upper(),names) # here i use spance" " so it's output is also with space but it's one string now



#Exercise 1
#i
#map - to apply a specific operation to all the element in a collection of iterable items. map(function(contains the task to apply to all elements one by one), iterable_Collection)
#filter - to filter element from a iterable collection base on a specific rules/condition implementation same as map
#reduce - to apply a operation on some specifi items of a iterable collection and then use it as the first value and add the whole sequence in the same harmoney and  make a single value

#Before Exercise 2 I'm gonna try some problem to understand how much i understand the higher order function

number = [23,12,32,6,6,34,65,242]
def apply_operation(lst):
    final_list = []
    def op(index,number):
        return index + " " + number
    for i in range(lst):
        final_list.append([op(i,lst[i])])
    return final_list

def square(num):
    return num*num

def cube(num):
    return cube**3

def calculation(num,func):
    print(func(num))

def calculation2(num,choice):
    if choice=='square':
        print(square(num=num))
    else:
        return cube(num)

# calculation2(5,'square')

#Exercise 1 - 3

mapped = map(square,number)
# print(list(mapped)) # like this we always need to use List converter to convert
def filter2(number):
    return number%2==0

filtered = filter(filter2,number)
filtered = list(filtered)

def for_reduce(a,b):
    return ((a+b))

reduced = reduce(for_reduce,filtered)

#question 1 - (4-6)
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 4. Use for loop to print each country
def print_func(lst):
    for i in lst:
        print(i)

print_func(countries)


# 5. Use for to print each name  
# 6. Use for to print each number


#same print_func will work for 5 & 6 also 

#level 2 
# 1
new_country = list(map(lambda country:country.upper(),countries))
print(new_country)

#2
square_numbers = list(map(lambda number : number**2,numbers))
print(square_numbers)

#3 - names one is also same as countries one .upper(

#4
land_countries = list(filter(lambda country:'land' in country,countries)) #can also use if-else logic with lambda
print(f"Country name containing (land) : {land_countries}")

#5
six_character_country = list(filter(lambda country:len(country)==6,countries))
print(f"six_character_country : {six_character_country}")

#6
six_letterandmore = list(filter(lambda country:len(country)>6 or len(country)==6,countries))
print(f"Country name containing six letter and more : {six_letterandmore}")

#7
starting_with_E = list(filter(lambda country:country.startswith('E'),countries))
print(f"Countris Start with (E) : {starting_with_E}")

#8
chain_implement =reduce(lambda a,b:a.upper()+' '+b.upper() ,list(filter(lambda country:len(country)>=7,(list(map(lambda country:country.title(),countries))))))
print(f"Implement of reduce(filter(map)) : {chain_implement}")

#9
string_list = list(filter(lambda x:type(x)==str,[23,'Hello',599,True,"Hey",False,False,'Hi',' ']))


#10
sum_reduce = reduce(lambda x,y:x+y,numbers)


#11
concatenate_string = reduce(lambda x,y:x+", "+y if y!=countries[-1] else x+', and ' + y + " are north European countries",countries)#there's a comma before and it's called 'Oxford Comma' the example answer tell to include so i add


from countries import countries as countries_2nd
#12
def categorize_country(lst,str):
    return list(filter(lambda x:str in x,lst))
# x = categorize_country(countries_2nd,'ia')
# y = categorize_country(countries_2nd,'ge')


#13
def categorize_country_2nd(lst):
    country_info = {}
    for i in lst:
        if (i[0]) not in country_info.keys():
            country_info[i[0]] = 1
        else:
            country_info[i[0]] +=1
    return country_info

x = categorize_country_2nd(countries_2nd)    
x = sorted(x.items(), key=lambda x:x[1], reverse=True)
def show_func():
    print(f"Index \t --- \t Country_Capital_name \t --- \t Count :")
    for i,(country,count) in enumerate (x,1):
        print(f"{i} \t --- \t {country} \t --- \t {count}")


#14 - no need to implement just slice the main countries list from 0 to 10 to get the first 10 countries
#15 - same same just slice -1,-11
#print(countries_2nd[-1:-11:-1])

#Level 3 
#1 - sort countries_data.py by name,capital and population

from sample import country_info
def sort_byname(lst):
    sorted_list = []
    for key in lst:
        sorted_list.append(key['name'])
    return set(sorted_list)    

sorted_final = list(sort_byname(country_info))
#for sorting those two methods are ok
# sorted_final = sorted(sorted_final)
sorted_final.sort()
print(sorted_final)

