"""6. Create a list with the names of friends and colleagues. Search for the
name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it."""

num=int(input("How many friends do you have: "))
friends=[]
for i in range(num):
    name=str(input("Enter the name: "))
    friends.append(name)
print(friends)

for i in friends:
    if i.title() =='John':
        print("Found")
        break
    else:
        print("not found")
        break