#1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

#we can do the list comprehension in line but functions will keep this organize i think as a beginner
def flaten_num(lst):
    flaten_lst = [i for i in lst if i > 0 and i != 0]
    return flaten_lst

#2 - list of lists of lists

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

def one_dimen_lst(lst):
    final_lst = [number for row in lst  for element in row for number in element] 

    #My Thoughts along the way to solve the question

    # secondary = [number for row in lst for number in row]
    # final_ = [number for row  in secondary for number in row]
    # final_lst = []
    # for i in lst:
    #     for j in i:
    #         for k in j:
    #             final_lst.append(k)

    print("final list : ",final_lst)
    return final_lst


#3 -> list of tuples

#for better understanding the logic try with loop first
def list_tuple(row,column):
    temp_list = []
    temp_tuple = []
    for i in range(0,row+1):
        
        for j in range(0,column):
            if j==0:
                temp_list.append(i)
            elif j==1:
                temp_list.append(1)
            else:
                temp_list.append(i**(j-1))
        temp_tuple.append(tuple(temp_list))
        temp_list.clear()

    return temp_tuple
    


#the full above code in list comprehension

x = [(i,1) + tuple(i**exp for exp in range(1,6)) for i in range(0,11)]

#print(x)



#list_tuple(10,7)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#first approach with normal loop to understand the problem 
def organize_countries(lst):
    final = []
    for i in lst:
        organize = []
        for j in i:
            '''
            this code block can be more cleaner and good
            x = j[0].upper()
            organize.append([x , x[0:3],j[1].upper()])
            '''
            organize.append(j[0].upper())
            x =(organize[0])
            x = x[0:3]
            organize.append(x)
            organize.append(j[1].upper())
        final.append((organize))
        
        
    
    print(final)


#2nd approach to implement it in list comprehension
# here first element goes inside the list countries then (country,city) they go inside the tuple and take the element from there
country_city = [list((country.upper(),country[0:3].upper(),city.upper())) for element in countries for (country,city) in element]


#5->list -> list of dictionary

def country_dic(lst):
    dic_country = {}
    final_list = []
    for i in lst:
        for j in i:
            dic_country={
                'country': j[0].upper(),
                'city' : j[1].upper()
            }
            
        final_list.append(dic_country)
    print(final_list)


country_dic1 = [{'country' : country.upper(),'city':city.upper()} for country_pair in countries for (country,city) in country_pair]

#it's more compact using tuple
country_dic2 = [{'country':country.upper(),'city':city.upper()} for [(country,city)] in countries]

#6 -list of lists  -> concatenated string

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

def ques_6(lst):
    temp = []
    for out_loop in lst:
        for (First,second) in out_loop:
            temp.append(First+ " "+second)
        
    print(temp)

#using list comprehension
ques_6_final = [f"{First_name} {surname}" for [(First_name,surname)] in names]


#7 - lambda function to calculate a slope or y-intercept of linear functions.


x = lambda x1,y1,x2,y2:((y2-y1)/(x2-x1))

calc_yintercept =  lambda m,x,y:y-(m*x)

print(x(1,2,3,4))
print(calc_yintercept(3,2,5))
def calc_fun():
