import string


alphabet = string.ascii_lowercase
print("1. Enc \n 2.Dec")

choice=int(input("Enter the choice : "))

while(True):

     if choice==1:

          def enc(text,s):
               result=""


          #transverse the plain text
               for i in range(len(text)):
                    char=text[i]

                    #upper case charecters
                    if(char.isupper()):
                         result+=chr((ord(char)+s-65)%26+65)

                    else:
                         #lower case charecters
                         result+=chr((ord(char)+s-97)%26+97)

               return result


          text=input("Enter the text : ")
          s= int(input("Enter the shift pattern : "))

          print("plain text : "+text)
          print("shift pattern : ",s)
          print("cipher : "+enc(text,s))

     elif choice==2:
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

     else:
          print("Wrong choice")
