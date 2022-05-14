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
