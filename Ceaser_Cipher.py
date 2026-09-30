alphabet = ["a" , "b" , "c" , "d" , "e" , "f", "g" , "h" ,"i" , "j" , "k" , "l" , "m" , "n" , "o" , "p" , "q" , "r" ,"s" , "t" , "u" , "v" , "w" , "x" ,"y" ,"z"]
numbers = ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9"]


#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n")
#text = input("Type in your message: \n").lower()
#shift = int(input("Type the shift number:\n"))

#def encrypt(original_text , shift_amount):
           #encrypted_word  = ""    
            #for letters in original_text:
                #find_e_index = alphabet.index(letters)
                #new_encrypt = find_e_index + shift_amount
                #new_encrypt %= len(alphabet)
                #new_e_letters = alphabet[new_encrypt]
                #encrypted_word += new_e_letters
            #print(f"Here is your encoded word: {encrypted_word}")

#def decrypt(orginal_text , shift_amount):
            #Tobe_decrypted_word = ""
            #for letters in orginal_text:
                #find_d_index = alphabet.index(letters)
                #solve_decrpyt = find_d_index - shift_amount
                #solve_decrpyt %= len(alphabet)
                #new_d_letters = alphabet[solve_decrpyt]
                #Tobe_decrypted_word += new_d_letters
            #print(f"Here is your decrypted word: {Tobe_decrypted_word}")


## WE made it great good job!!
## but the two functions are almost the same with one different line, so instead of combining and calling them in the ceaser function
## We can just make it so that ceaser function has both of the same parts and only changes the part that matters.



def ceaser(original_text , shift_amount, encode_or_decode):    
        output = ""
        if encode_or_decode == "decode":
                    shift_amount *= -1
        for letters in original_text:
            
            if letters not in alphabet:
                output += letters
            else:      
                
                find_index = alphabet.index(letters)
                total_shift = find_index + shift_amount
                total_shift %= len(alphabet)
                new_letters = alphabet[total_shift]
                output += new_letters
        print(f"Here is the {encode_or_decode}d result: {output}")
        

restart = "yes"

while restart == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n")
    text = input("Type in your message: \n").lower()
    shift = int(input("Type the shift number:\n"))

    ceaser(text, shift, direction)
    restart = input("Do you want to conitnue or not input 'Yes' or 'No'\n").lower()
    if restart == "no":
        print("Goodbye")
