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



