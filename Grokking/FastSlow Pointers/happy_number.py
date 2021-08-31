def find_happy(number):
    slow,fast=number, number
    while True:
        slow = find_square(slow)
        fast = find_square(find_square(fast))
        if slow == fast:
            break
    return slow == 1

def find_square(number):
    sum1=0
    while number>0:
        digit = number %10
        sum1=+ digit * digit
        number //= 10
    return sum1


print(find_happy(23)) 
print(find_happy(12)) 