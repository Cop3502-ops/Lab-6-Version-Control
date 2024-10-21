#Aatish Duddela and Vincent Hong
def encode(password):
    encodePassword = ""
    for digit in password:
        newDigit = (int(digit) + 3) % 10
        #The password is encoded by adding each individual digit by 3.
        #For two-digit numbers, the number is encoded using modulus 10 to get the last digit
        #Type-casting is needed because strings and integers alone do not concatenate with each other
        encodePassword += str(newDigit)

    return encodePassword

def decode(encoded):
    decoded = ""

    #takes each number in encoded and minus it by 3 and then adds that number as a string to the variable called decoded
    for num in encoded:
        decoded += str((int(num) - 3) % 10)

    return decoded

def main():
    continueCode = True
    while continueCode:
        print("Menu") #Prints the menu options
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")
        menuChoice = input("Please enter an option:") #Asks user for an option
        if menuChoice == "1":
            passEncoder = input("Please enter your password to encode:")
            encodeVar = encode(passEncoder)
            #Removed the print statement which displays the encoded password
            #print(encode(passEncoder))
            print("Your password has been encoded and stored!")
            print("") #Added a new line when reprinting the menu
        elif menuChoice == "2":
            decoded_pass = decode(encodeVar)
            print(f"The encoded password is {encodeVar}, and the original password is {decoded_pass}.\n")
        else:
            break
if __name__ == "__main__":
    main()
