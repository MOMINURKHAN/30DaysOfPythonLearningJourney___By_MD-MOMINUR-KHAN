#there are just playing with the examples
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable
#to fileter short name i mean to take short name and clear long ones 
x = filter(lambda n:len(n)<7,names)
#we can also use the logical operator here 
#x = filter(lambda n:n if len(n)<7 else False,names)
print(list(x)) #we need list to see the item

from functools import reduce
#try implementation of reduce function with lambda to add the all names together in the list names
x = reduce(lambda a,b,c:a.upper()+" "+b.upper() + c.upper(),names)
print(x)

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