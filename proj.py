import string,sys,random

from cryptography.fernet import Fernet

 

alphabetL = string.ascii_lowercase

alphabetU = string.ascii_uppercase

while(True):

    print("1.Encrypt a message using Caesar Cipher \n2.Decrypt a message using Caesar cipher\n3.Encrypt and Decrypt an encrypted message from a file using Caesar cipher \n(You will need a text file called 1.txt with your encrypted message in the text file)\n4.Encrypt and Decrypt using an Atbash cipher\n5. Encrypt and decrypt a message using monoalphabetic cipher\n6.Encrypt and decrypt a message using Vigenere cipher\n7. Encrypt and decrypt a message using Playfair cipher\n8.Exit ")

    choice=int(input("Enter the choice : "))        

    if choice==1:

 

          def enc(text,s):

               result=""

               for i in range(len(text)):

                    char=text[i]

                    #upper case charecters

                    if(char.isupper()):

                         result+=chr((ord(char)+s-65)%26+65)

 

                    elif (char.islower()):

                         #lower case charecters

                         result+=chr((ord(char)+s-97)%26+97)

                    else:

                        #result+=chr((ord(char)+s))

                        result+=char

               return result  

          text=input("Enter the text : ")

          s= int(input("Enter the shift pattern : "))

 

          print("plain text : "+text)

          print("shift pattern : ",s)

          print("Your encrypted cipher is: "+enc(text,s))

 

    elif choice==2:

          def decrypt():

              enc = input("Enter the message: ")

              key = int(input("Enter key : "))

              dec= ""

              for c in enc:

                  if c in alphabetU:

                      position = alphabetU.find(c)

                      new_pos = (position - key) % 26

                      new_char = alphabetU[new_pos]

                      dec+= new_char

                  elif c in alphabetL:

                      position = alphabetL.find(c)

                      new_pos = (position - key) % 26

                      new_char = alphabetL[new_pos]

                      dec+= new_char

                  else:

                      dec+= c

                  print("Encrypted message:",enc)

                  print("Shift pattern:",key)    

                  print("Your decrypted cipher is:",dec)

          decrypt()  

    elif choice==3:

        class Encryptor():

 

            def key_create(self):

                key = Fernet.generate_key()

                return key

 

            def key_write(self, key, key_name):

                with open(key_name, 'wb') as mykey:

                    mykey.write(key)

 

            def key_load(self, key_name):

                with open(key_name, 'rb') as mykey:

                    key = mykey.read()

                return key

 

            def file_encrypt(self, key, original_file, encrypted_file):

               

                f = Fernet(key)

 

                with open(original_file, 'rb') as file:

                    original = file.read()

 

                encrypted = f.encrypt(original)

 

                with open (encrypted_file, 'wb') as file:

                    file.write(encrypted)

 

            def file_decrypt(self, key, encrypted_file, decrypted_file):

               

                f = Fernet(key)

 

                with open(encrypted_file, 'rb') as file:

                    encrypted = file.read()

 

                decrypted = f.decrypt(encrypted)

 

                with open(decrypted_file, 'wb') as file:

                    file.write(decrypted)

 

            encryptor=Encryptor()

 

            mykey=encryptor.key_create()

 

            encryptor.key_write(mykey, 'mykey.key')

 

            loaded_key=encryptor.key_load('mykey.key')

 

            encryptor.file_encrypt(loaded_key, '1.txt', '2.txt')

 

            encryptor.file_decrypt(loaded_key, '2.txt', '1.txt')

 

    elif choice==4:    

        def Atbash_crypt(cistring):

            string = ""    

            cistring = formatString(cistring)

            for x in range(0, len(cistring)):

                string += flipChar(cistring[x])

            return(string)  

        def formatString (string):

            fmtString = string.lower()  

            fmtString = "".join(fmtString.split())  

            return fmtString          

        def flipChar(char):          

            flip = abs((ord(char) - 96) - 27)        

            return chr(flip + 96) if flip > 0 and flip <= 26 else ""

        def Atbash():        

            print("Atbash Cipher")

            print("-------------------------------")

            cistring = input("Please enter a text string below.  All numbers will be stripped.\n")

            print("\nThe starting string is:")

            print (cistring,"\n")

            print("The Atbash encrypted string is:")

            print(Atbash_crypt(cistring),"\n")

            print("The Atbash decrypted string is:")

            print(Atbash_crypt(Atbash_crypt(cistring)),"\n")          

        print(Atbash())

 

    elif choice==5:

        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        def main():

            myMessage =input("enter the message : ")

            myKey = 'QWERTYUIOPASDFGHJKLZXCVBNM'

            print("select the mode 'encrypt'  for encrypt and 'decrypt' for decrypt")

            myMode = input("enter the mode : ") # set to 'encrypt' or 'decrypt'

            checkValidKey(myKey)

            if myMode == 'encrypt':

                translated = encryptMessage(myKey, myMessage)

            elif myMode == 'decrypt':

                translated = decryptMessage(myKey, myMessage)

            print('Using key %s' % (myKey))

            print('The %sed message is:' % (myMode))

            print(translated)

        def checkValidKey(key):

            keyList = list(key)

            lettersList = list(LETTERS)

            keyList.sort()

            lettersList.sort()

            if keyList != lettersList:

                sys.exit('There is an error in the key or symbol set.')

        def encryptMessage(key, message):

            return translateMessage(key, message, 'encrypt')

        def decryptMessage(key, message):

            return translateMessage(key, message, 'decrypt')

        def translateMessage(key, message, mode):

            translated = ''

            charsA = LETTERS

            charsB = key

            if mode == 'decrypt':

           

                charsA, charsB = charsB, charsA

            # loop through each symbol in the message

            for symbol in message:

                if symbol.upper() in charsA:

                    # encrypt/decrypt the symbol

                    symIndex = charsA.find(symbol.upper())

                    if symbol.isupper():

                        translated += charsB[symIndex].upper()

                    else:

                        # symbol is not in LETTERS, just add it

                        translated += charsB[symIndex].lower()

                else:

                    translated += symbol

            return translated

        def getRandomKey():

            key = list(LETTERS)

            random.shuffle(key)

            return ''.join(key)

        main()

    elif choice==6:

        def generateKey(string, key):

            key = list(key)

            if len(string) == len(key):

                return(key)

            else:

                for i in range(len(string) -len(key)):

                    key.append(key[i % len(key)])

            return("" . join(key))

 

        def encryption(string, key):

            encrypt_text = []

            for i in range(len(string)):

                x = (ord(string[i]) +ord(key[i])) % 26

                x += ord('A')

                encrypt_text.append(chr(x))

            return("" . join(encrypt_text))

        def decryption(encrypt_text, key):

            orig_text = []

            for i in range(len(encrypt_text)):

                x = (ord(encrypt_text[i]) -ord(key[i]) + 26) % 26

                x += ord('A')

                orig_text.append(chr(x))

            return("" . join(orig_text))

        if __name__ == "__main__":

            string = input("Enter the message: ")

            keyword = input("Enter the keyword: ")

            key = generateKey(string, keyword)

            encrypt_text = encryption(string,key)

            print("Encrypted message:", encrypt_text)

            print("Decrypted message:", decryption(encrypt_text, key))

    elif choice==7:

        key=input("Enter key")

        key=key.replace(" ", "")

        key=key.upper()

 

        def matrix(x,y,initial):

            return [[initial for i in range(x)] for j in range(y)]

           

        result=list()

        for c in key: #storing key

            if c not in result:

                if c=='J':

                    result.append('I')

                else:

                    result.append(c)

        flag=0

        for i in range(65,91): #storing other character

            if chr(i) not in result:

                if i==73 and chr(74) not in result:

                    result.append("I")

                    flag=1

                elif flag==0 and i==73 or i==74:

                    pass    

                else:

                    result.append(chr(i))

        k=0

        my_matrix=matrix(5,5,0) #initialize matrix

        for i in range(0,5): #making matrix

            for j in range(0,5):

                my_matrix[i][j]=result[k]

                k+=1

        def locindex(c): #get location of each character

            loc=list()

            if c=='J':

                c='I'

            for i ,j in enumerate(my_matrix):

                for k,l in enumerate(j):

                    if c==l:

                        loc.append(i)

                        loc.append(k)

                        return loc                    

        def encrypt():  #Encryption

            msg=str(input("ENTER MSG:"))

            msg=msg.upper()

            msg=msg.replace(" ", "")            

            i=0

            for s in range(0,len(msg)+1,2):

                if s<len(msg)-1:

                    if msg[s]==msg[s+1]:

                        msg=msg[:s+1]+'X'+msg[s+1:]

            if len(msg)%2!=0:

                msg=msg[:]+'X'

            print("CIPHER TEXT:",end=' ')

            while i<len(msg):

                loc=list()

                loc=locindex(msg[i])

                loc1=list()

                loc1=locindex(msg[i+1])

                if loc[1]==loc1[1]:

                    print("{}{}".format(my_matrix[(loc[0]+1)%5][loc[1]],my_matrix[(loc1[0]+1)%5][loc1[1]]),end=' ')

                elif loc[0]==loc1[0]:

                    print("{}{}".format(my_matrix[loc[0]][(loc[1]+1)%5],my_matrix[loc1[0]][(loc1[1]+1)%5]),end=' ')  

                else:

                    print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    

                i=i+2                                

        def decrypt():  #decryption

            msg=str(input("ENTER CIPHER TEXT:"))

            msg=msg.upper()

            msg=msg.replace(" ", "")

            print("PLAIN TEXT:",end=' ')

            i=0

            while i<len(msg):

                loc=list()

                loc=locindex(msg[i])

                loc1=list()

                loc1=locindex(msg[i+1])

                if loc[1]==loc1[1]:

                    print("{}{}".format(my_matrix[(loc[0]-1)%5][loc[1]],my_matrix[(loc1[0]-1)%5][loc1[1]]),end=' ')

                elif loc[0]==loc1[0]:

                    print("{}{}".format(my_matrix[loc[0]][(loc[1]-1)%5],my_matrix[loc1[0]][(loc1[1]-1)%5]),end=' ')  

                else:

                    print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    

                i=i+2        

        while(1):

            choice=int(input("\n 1.Encryption \n 2.Decryption: \n 3.EXIT\n"))

            if choice==1:

                encrypt()

            elif choice==2:

                decrypt()

            elif choice==3:

                exit()

            else:

                print("Choose correct choice")

    elif choice==8:

        break

 

    else:

        print("Wrong choice, restart the program as we are exiting...")

        break

 