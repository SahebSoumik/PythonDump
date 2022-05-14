import string


alphabet = string.ascii_lowercase

def decrypt():
    
    
    enc = input("Enter the message: ")
    
    key = int(input("Enter key : "))
    
    dec= ""

    for c in enc:

        if c in alphabet:
            position = alphabet.find(c)
            new_pos = (position - key) % 26
            new_char = alphabet[new_pos]
            dec+= new_char
        else:
            dec+= c
    print(dec)

decrypt()
