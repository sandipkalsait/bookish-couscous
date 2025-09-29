#print and count the prime numbers in a given range

def is_prime(num):
    iterator=2
    middle=num//2
    
    if num<=1:
        return False
#    while iterator<=middle :
#        if num % iterator == 0 :
#            return False
#        iterator+=1
#        return True
      
    for iterator in range(2,num//2+1):
        if num % iterator == 0:
              return False
        else:
              return True
    

        
        
        

def get_prime_numbers(start,end):
    counter=0
    for num in range(start,end+1):
       if is_prime(num) :
           print(f"{num}",end=" ")
           counter+=1
    return counter

print("Printing and count the prime numbers in a given range")

print("Enter the range values")
x=int(input("Enter start value"))
y=int(input("Enter last value"))
count=get_prime_numbers(x,y)
print(f"\nCount of {count}")
