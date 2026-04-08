import re
txt = 'I love to teach python and javaScript 23 543 235 34 002 '
match = re.match('I love to teach python',txt,re.I)
print(match)
span = match.span()
print(span)
start,end = span
print(start,end)
hello = [23,43]
a,b = hello
print(a,b)

split = re.split(" ",txt)
print(f"this is split ;  {split}")
x,*y,z = split
print(x,y,z)

new = re.sub("love","hate",txt)
numbers = re.findall(r"\d",txt)
print("Numbers :" , numbers)
print(new)
txt2 = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
matches = re.findall('[pP]ython',txt2)
print( "Matches new : ",matches)
replace = re.sub('[P/p]ython','Javascript',txt2)
print(replace)
txt3 = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''
filtering = re.sub('%',"",txt3)
print(filtering)

text = "Phoone: 123-456-7890, Zip: 90210"
vowels = re.findall(r"\w+",text)
print(vowels)
dic = {'Category':vowels[-2:-1],'ID':vowels[-1:]}
vowels.sort()
s = re.match(r"pho?ne",text,re.I)
print(s)
print(dic,vowels)
emails = [
    "user@example.com",        # Valid
    "john.doe@gmail.com",      # Valid
    "invalid-email",            # Invalid
    "test@domain.co.uk",        # Valid
    "name@company"              # Invalid
]

normal = 'hellol'
normal_list = list(normal)
list = ['0' for i in range(0,len(normal))]
print(normal_list)
word = 'o'

if word in normal_list:
    for index,i in enumerate(normal_list):
            if i==word:
                    list[int(index)]=word
                    print(list)
                

#Exercise 1

#qs - what's the most frequent word in the following paragraph

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
dict_mostfrq = {'word':'count'}
for i in paragraph:
       dict_mostfrq["word" : i]

