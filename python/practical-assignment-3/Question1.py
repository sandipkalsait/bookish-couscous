# Create 2 lists L1 and L2 by accepting values from user.
# Perform following operations  on them 

# 1. Find L1-L2 
# 2. L2-L1 
# 3. Their Symmetric difference 

# Without using built-in any function of set class.

def accept():
    n = int(input(f"Enter number of elements for List : "))
    L = []
    for i in range(n):
        val = int(input(f"Enter List [{i+1}]: "))
        L.append(val)
    return L


L1=accept()
L2=accept()
# L1 - L2
diff_L1_L2 = []
for item in L1:
    if item not in L2 and item not in diff_L1_L2:
        diff_L1_L2.append(item)

# L2 - L1
diff_L2_L1 = []
for item in L2:
    if item not in L1 and item not in diff_L2_L1:
        diff_L2_L1.append(item)

# Symmetric Difference = (L1 - L2) + (L2 - L1)
sym_diff = diff_L1_L2 + diff_L2_L1


print("\nL1 elements:", L1)
print("L2 elements:", L2)
print("L1 - L2:", diff_L1_L2)
print("L2 - L1:", diff_L2_L1)
print("Symmetric Difference:", sym_diff)


# # Output
# PS C:\Users\kalsa\OneDrive\Backup storage\OneDrive\Desktop\MSc computer science\bookish-couscous\python\practical-assignment-3> & C:/Users/kalsa/AppData/Local/Microsoft/WindowsApps/python3.11.exe "c:/Users/kalsa/OneDrive/Backup storage/OneDrive/Desktop/MSc computer science/bookish-couscous/python/practical-assignment-3/Question1.py"
# Enter number of elements for List : 4 
# Enter List [1]: 32
# Enter List [2]: 32
# Enter List [3]: 21
# Enter List [4]: 3
# Enter number of elements for List : 5
# Enter List [1]: 32
# Enter List [2]: 22
# Enter List [3]: 1
# Enter List [4]: 3
# Enter List [5]: 4

# L1 elements: [32, 32, 21, 3]
# L2 elements: [32, 22, 1, 3, 4]
# L1 - L2: [21]
# L2 - L1: [22, 1, 4]
# Symmetric Difference: [21, 22, 1, 4]