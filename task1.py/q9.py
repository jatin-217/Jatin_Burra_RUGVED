def caesar_cipher_encrypt(text: str, shift: int) -> str:
    result = ""
    
    for char in text:
        if char.isupper():
            result +=chr((ord(char)-ord('A')+shift)%26+ord('A'))
        elif char.islower():
            result +=chr((ord(char)-ord('a')+shift)%26+ord('a'))
        else:
            result +=char
    
    return result

message =input("Enter the message:")
shift =int(input("Enter the shift value:"))
encrypted =caesar_cipher_encrypt(message,shift)
print("Encrypted message:",encrypted)


