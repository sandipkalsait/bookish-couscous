# 2. Create a menu driven functionality on list with following menus 
#     1. Create a list 
#     2. Add an element at the beginning of the list 
#     3. Add an element at the end of the list 
#     4. Remove element 
#     5. Display all the elements of the list. 
#     6. Exit 


def create_list():
    n = int(input("Count: "))
    return [input(f"Element {i+1}: ") for i in range(n)]

def add_begin(list_head):
    list_head.insert(0, input("Element: "))

def add_end(list_head):
    list_head.append(input("Element: "))

def remove_element(list_head):
    val = input("Element to remove: ")
    if val in list_head:
        list_head.remove(val)
    else:
        print("Not found")

def display(list_head):
    if not list_head:
        print("List is empty")
    else:
        print("List elements: (", end="")
        for item in list_head:
            print(item, end="")
            if item != list_head[-1]:
                print(", ", end="")
        print(")")

list_head = []

while True:
    print("""
          1.Create
          2.Add Begin
          3.Add End
          4.Remove
          5.Display
          0.Exit
          """)

    ch = int(input("Enter choice: "))
    if ch == 1:
        list_head = create_list()
    elif ch == 2:
        add_begin(list_head)
    elif ch == 3:
        add_end(list_head)
    elif ch == 4:
        remove_element(list_head)
    elif ch == 5:
        display(list_head)
    elif ch == 0:
        break
    else:
        print("Invalid choice")
