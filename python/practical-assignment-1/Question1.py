# Accpet the 'n' numbers from the users,
# store them in a list and print the maximum number
# without using the built-in function max()

def accept_numbers(n):
     list_of_numbers=list()
     for iterator in range( 0 , n ):
         list_of_numbers.append(int(input("Enter the number :\t")))
     return list_of_numbers

def get_max_number(list_of_numbers):
        max_number=0
        for number in list_of_numbers:
            if number > max_number :
                max_number=number
        return max_number

n=int(input("Enter how many numbers you want to enter :\t"))
list_of_numbers=accept_numbers(n)

print("The list of numbers is :")
print(list_of_numbers)
max_number=get_max_number(list_of_numbers)
print(f"The max number from list is :\t{max_number}")




