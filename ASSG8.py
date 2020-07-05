"""8. Write a function, is_prime, that takes an integer and returns True if
the number is prime and False if the number is not prime."""

def is_prime(val):
    if val>=2:
        for x in range(2,val):
            if not (val%x):
                return False
    else:
        return False
    return True

prim =int(input("Enter the value: "))
print(is_prime(prim))