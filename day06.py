tuples = (23,242,523,523,234)
_list = list(tuples)
print(tuples,  _list ,sep="\n")
print(tuples.count(23))
print(_list.count(23))

num1,num2,num3,num4,num5 = tuples
print(num1)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Norway' in nordic_countries)
print('Iceland' in nordic_countries)