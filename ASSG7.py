""" 7. Create a list of tuples of first name, last name, and age for your
friends and colleagues. If you don't know the age, put in None.
Calculate the average age, skipping over any None values. Print out
each name, followed by old or young if they are above or below the
average age."""

tup1=('ramesh','chaudhary',20)
tup2=('ritesh', 'prasai', 19)
tup3=('aman','magar',None)
tup4=('parmit','bhattarai',21)

friend_list=[]
friend_list.append(tup1)
friend_list.append(tup2)
friend_list.append(tup3)
friend_list.append(tup4)
# print(friend_list)

avg=[]
for tups in friend_list:
    if tups[2] != None:
        avg.append(tups[2])
print(avg)

print("The average i: "+str(sum(avg)/len(avg) ) )
