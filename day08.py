dog = {}
dog = {
    'Name' : 'Rocky',
    'Breed': 'Gernman Shephard',
    'Homland' : 'Helsinki',
    'Weight' : '28',
    'Colour' : ['red','green','yellow']

}

print(len(dog))
print(type(dog['Colour']))
print(dog.items())
print(dog.keys())
print(dog.get('Name'))
tuple1 = tuple(dog.keys())
tuple2 = tuple(dog.values())
tuple3 = tuple1 + tuple2
print(tuple3)
del dog['Name'] # deleting name
dog.pop('Colour') # deleting colour 
print(dog)
