#perfect numbers in given range

def is_perfect(number):
    
    if number<2:
        return False
    sum_of_div=1
    for iterator in range(2,number//2+1):
        if number % iterator == 0:
            sum_of_div+=iterator
        else:
            continue
            
    return sum_of_div == number

def get_perfect_numbers(start,end):
    counter=0
    for iterator in range(start,end+1):
        if is_perfect(iterator):
            print(f"{iterator}",end=", ")
            counter+=1
    return counter

print("Printing and count the perfect numbers in a given range")

print("Enter the range values ")
x=int(input("Enter start value "))
y=int(input("Enter last value "))
count=get_perfect_numbers(x,y)
print(f"\nCount of {count}")
