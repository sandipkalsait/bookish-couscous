def alphabet_pattern(rows):
    ch = ord('A')   # starting ASCII for A
    for i in range(1, rows+1):     
        for j in range(i):         
            if ch > ord('Z'):
                return
            print(chr(ch), end=" ")
            ch += 1
        print()   # new line


rows = int(input("Enter number of rows: "))
alphabet_pattern(rows)



def alphabet_pair_pattern(rows):
    ch = ord('A')   
    for i in range(1, rows+1):     
        for j in range(i):        
            if ch > ord('Z'):    
                return
            print(chr(ch) + chr(ch).lower(), end=" ")
            ch += 1
        print() 


rows = int(input("Enter number of rows: "))
alphabet_pair_pattern(rows)
