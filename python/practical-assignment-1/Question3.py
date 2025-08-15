# Create list of string &
# Count the ocurrence of each element
# Without using built-in function count()

def accept_strings(n):
     list_of_strings=[]
     for iterator in range( 0 , n ):
         list_of_strings.append(input("Enter the string :\t"))
     return list_of_strings

def count_occurences(list_of_string):
    occurences=dict()
    for element in list_of_string:
        if element in occurences:
            occurences[element]+=1
        else:
            occurences[element]=1
    return occurences


n=int(input("Enter how many strings you want to enter :\t"))
list_of_strings=accept_strings(n)

print("printing count of each occurnce in list ...")
print(count_occurences(list_of_strings))





