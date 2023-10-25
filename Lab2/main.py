def create_matrix(key):
    key = key.upper()
    matrix = [[0 for i in range (5)] for j in range(5)]
    letters_added = []
    row = 0
    col = 0
    # Adding the key to the matrix
    for letter in key:
        if letter not in letters_added:
            matrix[row][col] = letter
            letters_added.append(letter)
        else:
            continue
        if (col==4):
            col = 0
            row += 1
        else:
            col += 1
    
    # A=65 ... Z=90
    for letter in range(65,91):
        # Because we eliminate the J out of letter list, I/J are in the same position
        if letter==74: 
                continue
        if chr(letter) not in letters_added: 
            letters_added.append(chr(letter))
            
    
    index = 0
    for i in range(5):
        for j in range(5):
            matrix[i][j] = letters_added[index]
            index+=1
    return matrix

#Add X if the same letter is in a pair
def separate_same_letters(message):
    index = 0
    while (index<len(message)):
        l1 = message[index]
        if index == len(message)-1:
            message = message + 'X'
            index += 2
            continue
        l2 = message[index+1]
        if l1==l2:
            message = message[:index+1] + "X" + message[index+1:]
        index +=2   
    return message

def indexOf(letter,matrix):
    for i in range (5):
        try:
            index = matrix[i].index(letter)
            return (i,index)
        except:
            continue

def playfair(key, message, encrypt=True):
    inc = 1
    if encrypt==False:
        inc = -1
    matrix = create_matrix(key)
    message = message.upper()
    message = message.replace(' ','')    
    message = separate_same_letters(message)
    cipher_text=''
    for (l1, l2) in zip(message[0::2], message[1::2]):
        row1,col1 = indexOf(l1,matrix)
        row2,col2 = indexOf(l2,matrix)
        #Same Row Rule
        if row1==row2: 
            cipher_text += matrix[row1][(col1+inc)%5] + matrix[row2][(col2+inc)%5]
        #Same Column Rule
        elif col1==col2:
            cipher_text += matrix[(row1+inc)%5][col1] + matrix[(row2+inc)%5][col2]
        else: 
            cipher_text += matrix[row1][col2] + matrix[row2][col1]
    
    return cipher_text

def main():
    print("Please choose the option below:")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice not in [1, 2]:
        print("Invalid choice. Exiting...")
        return
    
    message = input("Write the message: ")
    key = input("Provide the key: ")
    
    if choice == 1:
        print("Encryption of the message: ")
        print( playfair(key, message))
    
    elif choice == 2:
        print("Decryption of the message: ")
        print( playfair(key, message, False))

if __name__=='__main__':
    main()
    
