## Decrypt a message with a specific dictionary
def decrypt_message(message, your_dict):
    decrypted_message = ""
    word = ""
    for index, c in enumerate(enc_message):
        print(c)
        if c.isspace():
            decrypted_message = decrypted_message + c
        elif c not in your_dict :
            decrypted_message = decrypted_message + c
        else :
            decrypted_message = decrypted_message + your_dict[c]
    return decrypted_message

## Populate a dictionary with the given couples
def populate_dictionary(keys, values):
    your_dictionary = {}
    for key, value in zip(keys, values):
        your_dictionary[key] = value
    return your_dictionary

## Example keys
keys = ['d', 'e', 'f','a','b','c']
## Example values
values = ['d', 'e', 'f']

## Open the input file
with open('encryptedMessage.txt', 'r') as file:
    enc_message = file.read().replace('\n', '')

## Populating the dictionary
dic = populate_dictionary(keys, values)
## Decrypting the message
dec_message = decrypt_message(enc_message, dic)

## Creating and saving the decrypted message in the output file.
text_file = open("decryptedMessage.txt", "w")
text_file.write(dec_message)
text_file.close()
