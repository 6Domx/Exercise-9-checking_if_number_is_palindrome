# Pseudocode
# 1. Create a program that will ask a user to input numbers
# 2. Analyze the number
# 3. Check to see if the number is palindrome
# 4. if yes return "TRUE"

while True:
    def given_is_palindrome(given_number):
        given_number = str(given_number)

        reversed_given_number = given_number[::-1]

        if given_number == reversed_given_number:
            return True
        else:
            return False
    
    given_number = input("Give us a number: ")
    if given_number.isdigit():
        given_number = int(given_number)

    else:
        print("Invalid, input must be number.")
        break

    if given_is_palindrome(given_number):
        print(given_number, "<- Palindrome!")
    else:
        print(given_number, "<- Not Palindrome!")
        break


