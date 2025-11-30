st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item23', 'item33'}
print( st2.difference(st1)) # set())
print(st1.difference(st2)) # {'item1', 'item4'} => st1\st2
print(st1.intersection(st2))
print(st1.isdisjoint(st2))
print(st1.symmetric_difference(st2))

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))
it_companies.add('Twitter')
it_companies.update(['Byd','Alibaba']) #while writing we need to use the square bracket inside the bracket
it_companies.remove("Facebook")
print('Companies set : ',it_companies)

C = A.union(B)
print(C)
print(A.intersection(B))
_string = "I am a teacher and I love to inspire and teach people. "
_string_update = list(_string)
print(_string_update)
print(len(_string_update))