import keyword
#declaring multiple variable in one signle line
first_name, last_name , age = "MD MOMINUR", "KHAN" , 23

print(age+2332)

print("hey",first_name,"Come come over here")
# print(keyword.kwlist)


print(keyword.iskeyword("False"))

for number in range(1,11):
    if number==7:
        continue
    print(number)