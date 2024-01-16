from Caesar_Cipher_logo import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    i = 0
    for char in text:
      if char not in alphabet:
        text[i] = char
      elif direction == 'encode':
        index = alphabet.index(char)
        text[i] = alphabet[index+(shift%26)-26]# to prevent out of index error like in case of civilization
      else:
        index = alphabet.index(char)
        text[i] = alphabet[index-(shift%26)-26]
      i+=1
#What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).

should_end = False
while not should_end:
#Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  if direction != 'encode' and direction != 'decode':
    print("You have entered wrong encryption methon, try again")
    continue
  text = list(input("Type your message:\n").lower())
  shift = int(input("Type the shift number:\n"))


  caesar(text, shift, direction)
  print("The message is: ", end=" ")
  print("".join(text))
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Gameover.")
  