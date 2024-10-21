#Aatish Duddela and Vincent Hong
def encode(password):
    encodePassword = ""
    for digit in password:
        newDigit = (int(digit) + 3) % 10
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
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")
        menuChoice = input("Please enter an option:")
        if menuChoice == "1":
            passEncoder = input("Please enter your password to encode:")
            encodeVar = encode(passEncoder)
<<<<<<< HEAD
=======
            #Removed the print statement which displays the encoded password
            #print(encode(passEncoder))
>>>>>>> 28330bece7ab8656ebe9d0e9c18a18f4d94a2051
            print("Your password has been encoded and stored!")
            print("")
        elif menuChoice == "2":
            decoded_pass = decode(encodeVar)
            print(f"The encoded password is {encodeVar}, and the original password is {decoded_pass}.\n")
        else:
            break
if __name__ == "__main__":
    main()
