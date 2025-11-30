#qs 1

str1 = 'thirty'
str2 = 'days'
str3 = 'of'
str4 = 'Python'
single_str = (f"{str1} {str2} {str3} {str4}")
print(len(single_str))
print(single_str.capitalize())
print(single_str.casefold())
#print(single_str.index(0,12,1))
print(single_str[0:12:1])
print(single_str[::2])
single_str.split("py")
new_string = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(new_string.split(","))
print(new_string.isidentifier())

check = '''I am enjoying this challenge.
I just wonder what is next.'''
print(check)

print('{} + {} =  {}'.format(8,6,8+6)) 
print('%d + %f = %s %d)'.format(8,14,"Hello",22))



