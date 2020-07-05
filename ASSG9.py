"""9. Write a binary search function. It should take a sorted sequence and
the item it is looking for. It should return the index of the item if found.
It should return -1 if the item is not found."""


def binary_search(sorted_sequence, item):
    for val in (sorted_sequence):
        if val.lower() ==item.lower():
            ind =sorted_sequence.index(val)
            return ind
        else:
            return -1



list=[]
vals=str(input("Enter the items with a space in between: "))
val = vals.split(" ")
sorted_val=sorted(val)
print(sorted_val)
sort_item=str(input("Enter the item you want to search: "))

output  =binary_search(sorted_val,sort_item)

print(output)
