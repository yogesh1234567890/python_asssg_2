"""5. Create a tuple with your first name, last name, and age. Create a list,
people, and append your tuple to it. Make more tuples with the
corresponding information from your friends and append them to the
list. Sort the list. When you learn about sort method, you can use the
key parameter to sort by any field in the tuple, first name, last name,
or age."""

tup1 = ('yogesh', 'bhattarai', 19)
tup2 = ('Dilisha', 'Maharjan', 20)
tup3 = ('Roshan', 'kc', 34)
tup4 = ('Chandani', 'Khatri', 19)
people=[]
people.append(tup1)
people.append(tup2)
people.append(tup3)
people.append(tup4)
print(people)

output=sorted(people, key=lambda x:x[0])
print(output)