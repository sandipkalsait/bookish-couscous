# Create list of Strings by accepting input from user
# Ask user which element user wants to remove.
# Remove the element and store then in another list
# Print the Output of both lists

def accept_strings(n):
     list_of_strings=[]
     for iterator in range( 0 , n ):
         list_of_strings.append(input("Enter the string :\t"))
     return list_of_strings

# remove the element and add it in 2nd list return both

def update_list(list1,list2,element):
    list1.remove(element)
    list2.append(element)
    return list1,list2

number=int(input("Enter how many strings you want to enter :\t"))
list1=accept_strings(number)
list2=[]


element=input("Enter the string you want to remove :\t")
if element in list1:
    list1,list2=update_list(list1,list2,element)
    print(f"The list1 is : {list1}")
    print(f"The list2 is : {list2}")
else:
    print(f"The string {element} is not in list : {list1}")

