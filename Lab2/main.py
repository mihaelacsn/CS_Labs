def toUpperCase(text):
    return text.upper()

def removeSpaces(text):
    newText = ""
    for i in text:
        if i == " ":
            continue
        else:
            newText = newText + i
    return newText

def Diagraph(text):
    Diagraph = []
    group = 0
    for i in range(1, len(text), 2): 
        Diagraph.append(text[group:i+2])  
        group = i+1
    if group < len(text):  
        Diagraph.append(text[group] + 'x')  
    return Diagraph


def FillerLetter(text):
    k = len(text)
    new_word = text

    if k % 2 == 0:
        for i in range(0, k, 2):
            if text[i] == text[i + 1]:
                new_word = text[0:i + 1] + str('x') + text[i + 1:]
                new_word = FillerLetter(new_word)
                break
    else:
        for i in range(0, k - 1, 2):
            if text[i] == text[i + 1]:
                new_word = text[0:i + 1] + str('x') + text[i + 1:]
                new_word = FillerLetter(new_word)
                break

    return new_word


list1 = ['A', 'Ă', 'Â', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'î', 'K', 'L', 'M',
         'N', 'O', 'P', 'Q', 'R', 'S', 'Ș', 'T', 'Ț', 'U', 'V', 'W', 'X', 'Y', 'Z']

def generateKeyTable(word, list1):
    key_letters = []
    for i in word:
        if i not in key_letters:
            key_letters.append(i)

    compElements = []
    for i in key_letters:
        if i not in compElements:
            compElements.append(i)
    for i in list1:
        if i not in compElements:
            compElements.append(i)

    matrix = []
    while compElements != []:
        matrix.append(compElements[:6])
        compElements = compElements[6:]

    return matrix

def search(mat, element):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == element:
                return i, j
    return None, None  


def encrypt_RowRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1c == 5:
        char1 = matr[e1r][0]
    else:
        char1 = matr[e1r][e1c + 1]

    char2 = ''
    if e2c == 5:
        char2 = matr[e2r][0]
    else:
        char2 = matr[e2r][e2c + 1]

    return char1, char2

def encrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1r == 5:
        char1 = matr[0][e1c]
    else:
        char1 = matr[e1r + 1][e1c]

    char2 = ''
    if e2r == 5:
        char2 = matr[0][e2c]
    else:
        char2 = matr[e2r + 1][e2c]

    return char1, char2

def encrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    char1 = matr[e1r][e2c]

    char2 = ''
    char2 = matr[e2r][e1c]

    return char1, char2

def encryptByPlayfairCipher(Matrix, plainList):
    CipherText = []
    for i in range(0, len(plainList)):
        c1, c2 = '', ''
        ele1_x, ele1_y = search(Matrix, plainList[i][0])
        ele2_x, ele2_y = search(Matrix, plainList[i][1])

        if ele1_x is not None and ele1_y is not None and ele2_x is not None and ele2_y is not None:
            if ele1_x == ele2_x:
                c1, c2 = encrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
            elif ele1_y == ele2_y:
                c1, c2 = encrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
            else:
                c1, c2 = encrypt_RectangleRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)

            cipher = c1 + c2
            CipherText.append(cipher)
        else:
            print(f"Element not found in matrix for pair: {plainList[i]}")

    return CipherText

def decrypt_RowRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1c == 0:
        char1 = matr[e1r][6]
    else:
        char1 = matr[e1r][e1c - 1]

    char2 = ''
    if e2c == 0:
        char2 = matr[e2r][6]
    else:
        char2 = matr[e2r][e2c - 1]

    return char1, char2

def decrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1r == 0:
        char1 = matr[6][e1c]
    else:
        char1 = matr[e1r - 1][e1c]

    char2 = ''
    if e2r == 0:
        char2 = matr[6][e2c]
    else:
        char2 = matr[e2r - 1][e2c]

    return char1, char2

def decrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
    char1 = matr[e1r][e2c]
    char2 = matr[e2r][e1c]

    return char1, char2

def decryptByPlayfairCipher(Matrix, cipherList):
    PlainText = []
    for i in range(0, len(cipherList)):
        c1 = 0
        c2 = 0
        ele1_x, ele1_y = search(Matrix, cipherList[i][0])
        ele2_x, ele2_y = search(Matrix, cipherList[i][1])

        if ele1_x == ele2_x:
            c1, c2 = decrypt_RowRule(Matrix, ele1_x, (ele1_y - 1) % 6, ele2_x, (ele2_y - 1) % 6)
        elif ele1_y == ele2_y:
            c1, c2 = decrypt_ColumnRule(Matrix, (ele1_x - 1) % 6, ele1_y, (ele2_x - 1) % 6, ele2_y)
        else:
            c1, c2 = decrypt_RectangleRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)

        plain = c1 + c2
        PlainText.append(plain)
    return PlainText

def validate_input(input_text, allowed_chars):
    for char in input_text:
        if char not in allowed_chars:
            return False
    return True

def main():
    print("1. Encrypt")
    print("2. Decrypt")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice not in [1, 2]:
        print("Invalid choice. Exiting.")
        return

    text_Plain = input("Enter the plain text: ")
    if not validate_input(text_Plain, list1):
        print(f"Invalid characters in the plain text. Allowed characters are: {', '.join(list1)}")
        return

    text_Plain = removeSpaces(toUpperCase(text_Plain))
    text_Plain = FillerLetter(text_Plain)  
    PlainTextList = Diagraph(text_Plain)

    key = input("Enter the key: ")
    if not validate_input(key, list1):
        print(f"Invalid characters in the key. Allowed characters are: {', '.join(list1)}")
        return

    print("Key text:", key)
    key = toUpperCase(key)
    Matrix = generateKeyTable(key, list1)

    if choice == 1:
        CipherList = encryptByPlayfairCipher(Matrix, PlainTextList)
        CipherText = ""
        for i in CipherList:
            CipherText += i
        print("CipherText:", CipherText)
    elif choice == 2:
        PlainTextList = decryptByPlayfairCipher(Matrix, PlainTextList)
        PlainText = ""
        for i in PlainTextList:
            PlainText += i
        print("PlainText:", PlainText)

if __name__ == "__main__":
    main()
