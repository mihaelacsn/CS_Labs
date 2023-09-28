def get_string(x):
    return x
def remove_duplicate(input_string):
    result = ""

    seen = set()
   
    for char in input_string:
        if char not in seen:
            result += char
            seen.add(char)
    
    return result

def main():
    custom_alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher_key = custom_alphabet
    input_text = ""
    output_text = ""
    second_key = ""
    operation = input("Choose your fighter:\n [e] Encryptor\n [d] Decryptor\n [x] Encryptor Two Keys\n [y] Decryptor Two Keys\n")
    input_text = input("Enter the text to process:\n")
    shift_key = int(input("Enter the shift key:\n"))
    output_text = input_text
    
    if operation == 'e':
        for i in range(len(custom_alphabet)):
            for j in range(len(output_text)):
                if custom_alphabet[i] == input_text[j]:
                    output_text = output_text[:j] + custom_alphabet[(i + shift_key) % 26] + output_text[j + 1:]
                elif custom_alphabet[i] == input_text[j].lower():
                    output_text = output_text[:j] + custom_alphabet[(i + shift_key) % 26].upper() + output_text[j + 1:]
    
    elif operation == 'd':
        for i in range(len(custom_alphabet)):
            for j in range(len(output_text)):
                if custom_alphabet[i] == input_text[j]:
                    output_text = output_text[:j] + custom_alphabet[(26 + i - shift_key) % 26] + output_text[j + 1:]
                elif custom_alphabet[i] == input_text[j].lower():
                    output_text = output_text[:j] + custom_alphabet[(26 + i - shift_key) % 26].upper() + output_text[j + 1:]
    
    elif operation == 'x':
        second_key = input("Enter the second key:\n")
        combined_key = second_key + cipher_key
        cipher_key = remove_duplicate(combined_key)
        
        print("The modified alphabet is:", cipher_key)
        
        for i in range(len(custom_alphabet)):
            for j in range(len(output_text)):
                if custom_alphabet[i] == input_text[j]:
                    output_text = output_text[:j] + cipher_key[(i + shift_key) % 26] + output_text[j + 1:]
                elif custom_alphabet[i] == input_text[j].lower():
                    output_text = output_text[:j] + cipher_key[(i + shift_key) % 26].upper() + output_text[j + 1:]
    
    elif operation == 'y':
        second_key = input("Enter the second key:\n")
        combined_key = second_key + cipher_key
        cipher_key = remove_duplicate(combined_key)
        
        print("The modified alphabet is:", cipher_key)
        
        for i in range(len(cipher_key)):
            for j in range(len(output_text)):
                if cipher_key[i] == input_text[j]:
                    output_text = output_text[:j] + custom_alphabet[(26 + i - shift_key) % 26] + output_text[j + 1:]
                elif cipher_key[i] == input_text[j].lower():
                    output_text = output_text[:j] + custom_alphabet[(26 + i - shift_key) % 26].upper() + output_text[j + 1:]
    
    print(output_text)

if __name__ == "__main__":
    main()
