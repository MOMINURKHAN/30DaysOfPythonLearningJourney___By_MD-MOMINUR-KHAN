_list = list()
print(_list)
_list1 = []
print(_list1)
_list1.append(_list)
_list.append(43)
print(_list1)

student_list = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
student_list.append(233)
student_list.append(32)
update_list = student_list.copy()
update_list.sort()
print(update_list)
length =int( len(update_list)/2)
print("Length of the list : ",len(update_list))
print("1st middle item : ",update_list[length] , "2nd middle item : ",update_list[length+1],sep="\n")
if length%2==0:
    print("Even :",update_list[length] + update_list[length+1])
else:
    print("Odds : ",update_list[length])
