#Exercise of day 03


for number in range(-100,100,1):
    x = number
    y = (x**2 + (6*x) + 9)

    if y==1:
        print("x :" ,x)

    
length_1 = len("Python")
length_2 = len("Dragon")

print(length_1==length_2)

if "on" in "Python" and "Dragon":
    print(True)

check = "on" in "I hope this course is not full of jargon"
print("Check : ", check)

if "on" not in "Python" and "Dragon":
    print("2nd :" ,True)
else:
    print(False)

float_value = float(length_1)
print(type(float_value))
string_value = str(float_value)
print(type(string_value))
if 7//3 == 7/3:
    print("7//3 == 7/3 :",True)
else:
    print("7//3 == 7/3 :",False)

if type('10')==type(10):
    print("'10' == 10 : " ,True)
else:
    print("'10' == 10 : " ,False)


# Working_Hour = int(input("Enter your working hour : "))
# Per_hour_Charge = int(input("Enter per hour charge : "))
# print("Your today's salary is : ", Working_Hour*Per_hour_Charge)

#here comes the most critical question of day03

list1 = [1,2,3,4,5]
list2 = [1,1,1,1,1]
list3=[]  
list4 = [] 
list5 = []
for number in range(0,5):
    num3 = list1[number] * list2[number]
    list3.append(num3)
for num in range(0,5):
    num4 = list1[num] * list3[num]
    list4.append(num4)
for num in range(0,5):
    num5 = list3[num] * list4[num]
    list5.append(num5)

for number in range(0,5):
    #this method didn't work for my target goal/work/task
    # if number==1:
    #     print(list1 ,sep= " ",end= " ")
    # if number==2:
    #     print(list2)
    # if number==3:
    #     print(list3)
    # if number==4:
    #     print(list4)
    # if number==5:
    #     print(list5)
    print(list1[number],list2[number],list3[number],list4[number],list5[number],sep="\t ",end="\n") # after trying several methods this one is working

  
_list = [list1,list2,list3,list4,list5]
print("_list : ",_list[list1[1]])
print("_list : ",_list[list1[0]])
print("_list : ",_list[list1[2]])
print("_list : ",_list[list1[3]])
#this is a good learning here _list[list1[1]] = _list[2] as because list1[1] = 2 the 2nd element of 1st list 
#                                   and _list[2] is actually the 2nd list here so it prints the whole 2nd list
for n in range(0,5):
    print(_list[0][n],_list[1][n],_list[2][n],_list[3][n],_list[4][n],sep=" ",end="\n")





""" while answer the last most complicated  question of the day, I found several solution
1. we can use for loop and make another loop with append the newly gotten value
        then we can just print all the list by a for loop first the first element of every
        list then the 2nd and so on. using 'sep' func to sep them 

2. after making and  appending in the lists we can also make another list that consist of 
all the list then using the for loop we can print the last list
    list[0][n],list[1][n] here n is the loop controler 0 to 4 and every iteration it'll change 
    and give the 2nd value , 3rd and 4th and so on .
    ***but need to careful about the syntax list[list1[1]] and list[0][0] these are totally different meaning


"""