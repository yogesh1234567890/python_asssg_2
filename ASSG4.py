"""4. Create a list. Append the names of your colleagues and friends to it.
Has the id of the list changed? Sort the list. What is the first item on
the list? What is the second item on the list?"""

list = ['yogesh' , 'Ramesh']
print(id(list))
names = str(input("Enter my friends name with space separating them: "))
val = names.split(' ')
list += val
print(id(list))

list.sort()
print(list)
#The id of the list remains the same
#The first item on the list is yogesh and second item is Ramesh.
