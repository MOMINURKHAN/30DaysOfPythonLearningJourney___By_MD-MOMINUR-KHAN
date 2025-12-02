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





#list_tuple(10,7)

# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# update = [(country[0].upper(),country) for data in countries for country in data]
# print(update)