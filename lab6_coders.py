#Aatish Duddela
def encode(password):
    encodePassword = ""
    for digit in password:
        newDigit = (int(digit) + 3) % 10
        encodePassword += str(newDigit)

    return encodePassword

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
            encode(passEncoder)
            print(encode(passEncoder))
            print("Your password has been encoded and stored!")

        elif menuChoice == "2":
            pass

        else:
            break
if __name__ == "__main__":
    main()
