# The Set :
'''
what is a set ?
for the set we keep a large amount of data in a single variable

1. to declare the set : '{' '}'
2. we cannot change value inside of the set
3. the set is unordered
'''
demoset={'bird','tiger','lion','dog','cat'}

print(demoset)

#insert a value

demoset.add('crocodile')

print(demoset)

#delete a value

demoset.remove('cat')

print(demoset)

# adding two sets

set1={'mobile','laptop','pc','printer'}

set2={'book','pen','pencile','bag'}

set3=set1.union(set2)

print(set3)








