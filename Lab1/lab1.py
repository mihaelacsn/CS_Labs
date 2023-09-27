def get_string(x):
    return x

def remove_duplicate(input_str):
    result = input_str[0]
    is_duplicate = False
    
    for i in range(1, len(input_str)):
        for j in range(len(result)):
            if input_str[i] == result[j]:
                is_duplicate = True
        
        if not is_duplicate:
            result += input_str[i]
        else:
            is_duplicate = False
    
    return result

def main():
    custom_alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher_key = custom_alphabet
    input_text = ""
    output_text = ""
    second_key = ""
    operation = input("Choose an operation:\n [e] Encrypt\n [d] Decrypt\n [e2] Two Keys\n [d2] Decrypt Two Keys\n")
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
    
    elif operation == 'e2':
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
    
    elif operation == 'd2':
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
